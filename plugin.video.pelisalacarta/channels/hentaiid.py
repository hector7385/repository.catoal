# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
# ------------------------------------------------------------

import re
import urlparse

from core import logger
from core import scrapertools
from core import servertools
from core.item import Item

CHANNEL_HOST = "http://hentai-id.tv/"


def mainlist(item):
    logger.info()

    itemlist = list()
    itemlist.append(Item(channel=item.channel, action="series", title="Novedades",
                         url=urlparse.urljoin(CHANNEL_HOST, "archivos/h2/")))
    itemlist.append(Item(channel=item.channel, action="letras", title="Por orden alfabético"))
    itemlist.append(Item(channel=item.channel, action="generos", title="Por géneros", url=CHANNEL_HOST))
    itemlist.append(Item(channel=item.channel, action="series", title="Sin Censura",
                         url=urlparse.urljoin(CHANNEL_HOST, "archivos/sin-censura/")))
    itemlist.append(Item(channel=item.channel, action="series", title="High Definition",
                         url=urlparse.urljoin(CHANNEL_HOST, "archivos/hight-definition/")))
    itemlist.append(Item(channel=item.channel, action="series", title="Mejores Hentais",
                         url=urlparse.urljoin(CHANNEL_HOST, "archivos/ranking-hentai/")))
    itemlist.append(Item(channel=item.channel, action="search", title="Buscar",
                         url=urlparse.urljoin(CHANNEL_HOST, "?s=")))

    return itemlist


def letras(item):
    logger.info()

    itemlist = []

    for letra in '0ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        itemlist.append(Item(channel=item.channel, action="series", title=letra,
                             url=urlparse.urljoin(CHANNEL_HOST, "/?s=letra-{0}".format(letra.replace("0", "num")))))

    return itemlist


def generos(item):
    logger.info()

    itemlist = []
    data = scrapertools.cache_page(item.url)
    data = re.sub(r"\n|\r|\t|\s{2}", "", data)

    data = scrapertools.get_match(data, "<div class='cccon'>(.*?)</div><div id=\"myslides\">")
    patron = "<a.+? href='/([^']+)'>(.*?)</a>"
    matches = re.compile(patron, re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle in matches:
        title = scrapertools.entityunescape(scrapedtitle)
        url = urlparse.urljoin(item.url, scrapedurl)
        logger.debug("title=[{0}], url=[{1}]".format(title, url))

        itemlist.append(Item(channel=item.channel, action="series", title=title, url=url))

    return itemlist


def search(item, texto):
    logger.info()
    if item.url == "":
        item.url = urlparse.urljoin(CHANNEL_HOST, "animes/?buscar=")
    texto = texto.replace(" ", "+")
    item.url = "{0}{1}".format(item.url, texto)
    return series(item)


def series(item):
    logger.info()

    data = scrapertools.cache_page(item.url)

    patron = '<div class="post" id="post"[^<]+<center><h1 class="post-title entry-title"[^<]+<a href="([^"]+)">' \
             '(.*?)</a>[^<]+</h1></center>[^<]+<div[^<]+</div>[^<]+<div[^<]+<div.+?<img src="([^"]+)"'

    matches = re.compile(patron, re.DOTALL).findall(data)
    itemlist = []

    for scrapedurl, scrapedtitle, scrapedthumbnail in matches:
        title = scrapertools.unescape(scrapedtitle)
        fulltitle = title
        url = urlparse.urljoin(item.url, scrapedurl)
        thumbnail = urlparse.urljoin(item.url, scrapedthumbnail)
        show = title
        logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))
        itemlist.append(Item(channel=item.channel, action="episodios", title=title, url=url, thumbnail=thumbnail,
                             show=show, fulltitle=fulltitle, fanart=thumbnail, folder=True))

    patron = '</span><a class="page larger" href="([^"]+)"'
    matches = re.compile(patron, re.DOTALL).findall(data)
    for match in matches:
        if len(matches) > 0:
            scrapedurl = match
            scrapedtitle = ">> Pagina Siguiente"

            itemlist.append(Item(channel=item.channel, action="series", title=scrapedtitle, url=scrapedurl,
                                 folder=True, viewmode="movies_with_plot"))

    return itemlist


def episodios(item):
    logger.info()
    itemlist = []

    data = scrapertools.cache_page(item.url)
    data = scrapertools.find_single_match(data, '<div class="listanime">(.*?)</div>')
    patron = '<a href="([^"]+)">([^<]+)</a>'
    matches = re.compile(patron, re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle in matches:
        title = scrapertools.unescape(scrapedtitle)
        url = urlparse.urljoin(item.url, scrapedurl)
        thumbnail = item.thumbnail
        plot = item.plot

        logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))

        itemlist.append(Item(channel=item.channel, action="findvideos", title=title, url=url,
                             thumbnail=thumbnail, plot=plot, show=item.show, fulltitle="{0} {1}"
                             .format(item.show, title), fanart=thumbnail, viewmode="movies_with_plot", folder=True))

    return itemlist


def findvideos(item):
    logger.info()

    data = scrapertools.cache_page(item.url)
    patron = '<div id="tab\d".+?>[^<]+<iframe.*?src="([^"]+)"'
    matches = re.compile(patron, re.DOTALL).findall(data)

    itemlist = []

    for scrapedurl in matches:
        title = "Ver en {0}".format(scrapertools.find_single_match(scrapedurl, 'http[s]?://([^/]+)'))

        itemlist.append(Item(channel=item.channel, action="play", title=title, url=scrapedurl, show=item.show,
                             fulltitle=item.title))

    return itemlist


def play(item):
    logger.info()
    itemlist = servertools.find_video_items(data=item.url)

    for videoitem in itemlist:
        if item.fulltitle:
            videoitem = item.fulltitle
        else:
            videoitem.title = item.title
        videoitem.channel = item.channel

    return itemlist
