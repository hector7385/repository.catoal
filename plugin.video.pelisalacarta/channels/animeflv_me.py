# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
# ------------------------------------------------------------

import os
import re
import sys
import urlparse

from channels import renumbertools
from core import config
from core import logger
from core import scrapertools
from core.item import Item

CHANNEL_HOST = "http://animeflv.me/"
CHANNEL_DEFAULT_HEADERS = [
    ["User-Agent", "Mozilla/5.0"],
    ["Accept-Encoding", "gzip, deflate"],
    ["Referer", CHANNEL_HOST]
]
header_string = "|User-Agent=Mozilla/5.0" \
                "&Referer=http://animeflv.me&Cookie="


def mainlist(item):
    logger.info()

    itemlist = list()

    itemlist.append(Item(channel=item.channel, action="letras", title="Por orden alfabético",
                         url=urlparse.urljoin(CHANNEL_HOST, "ListadeAnime")))
    itemlist.append(Item(channel=item.channel, action="generos", title="Por géneros",
                         url=urlparse.urljoin(CHANNEL_HOST, "ListadeAnime")))
    itemlist.append(Item(channel=item.channel, action="series", title="Por popularidad",
                         url=urlparse.urljoin(CHANNEL_HOST, "/ListadeAnime/MasVisto")))
    itemlist.append(Item(channel=item.channel, action="series", title="Novedades",
                         url=urlparse.urljoin(CHANNEL_HOST, "ListadeAnime/LatestUpdate")))
    itemlist.append(Item(channel=item.channel, action="search", title="Buscar...",
                         url=urlparse.urljoin(CHANNEL_HOST, "Buscar?s=")))

    if renumbertools.context:
        itemlist = renumbertools.show_option(item.channel, itemlist)

    return itemlist


def letras(item):
    logger.info()

    itemlist = []

    data = scrapertools.anti_cloudflare(item.url, headers=CHANNEL_DEFAULT_HEADERS, host=CHANNEL_HOST)
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;|<Br>|<BR>|<br>|<br/>|<br />|-\s", "", data)

    data = scrapertools.get_match(data, '<div class="alphabet">(.+?)</div>')
    patron = '<a href="([^"]+)[^>]+>([^<]+)</a>'
    matches = re.compile(patron, re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle in matches:
        title = scrapertools.entityunescape(scrapedtitle)
        url = urlparse.urljoin(item.url, scrapedurl)
        thumbnail = ""
        plot = ""
        logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))

        itemlist.append(Item(channel=item.channel, action="series", title=title, url=url, thumbnail=thumbnail,
                             plot=plot, viewmode="movies_with_plot"))

    return itemlist


def generos(item):
    logger.info()

    itemlist = []
    data = scrapertools.anti_cloudflare(item.url, headers=CHANNEL_DEFAULT_HEADERS, host=CHANNEL_HOST)
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;|<Br>|<BR>|<br>|<br/>|<br />|-\s", "", data)

    data = scrapertools.get_match(data, '<div class="barTitle">Buscar por género</div><div class="barContent">' +
                                  '<div class="arrow-general"></div><div>(.*?)</div>')
    patron = '<a href="([^"]+)[^>]+>([^<]+)</a>'
    matches = re.compile(patron, re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle in matches:
        title = scrapedtitle.strip()
        url = urlparse.urljoin(item.url, scrapedurl)
        thumbnail = ""
        plot = ""
        logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))

        itemlist.append(Item(channel=item.channel, action="series", title=title, url=url, thumbnail=thumbnail,
                             plot=plot, viewmode="movies_with_plot"))

    return itemlist


def search(item, texto):
    logger.info()

    texto = texto.replace(" ", "%20")
    item.url = "{0}{1}".format(item.url, texto)
    try:
        return series(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []


def series(item):
    logger.info()

    data = scrapertools.anti_cloudflare(item.url, headers=CHANNEL_DEFAULT_HEADERS, host=CHANNEL_HOST)
    head = header_string + get_cookie_value()

    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;|<Br>|<BR>|<br>|<br/>|<br />|-\s", "", data)

    patron = "<td title='<img.+?src=\"([^\"]+)\".+?<a.+?href=\"([^\"]+)\">(.*?)</a><p>(.*?)</p>"
    matches = re.compile(patron, re.DOTALL).findall(data)
    itemlist = []

    for scrapedthumbnail, scrapedurl, scrapedtitle, scrapedplot in matches:
        title = scrapedtitle.strip()  # scrapertools.unescape(scrapedtitle)
        url = urlparse.urljoin(item.url, scrapedurl)
        thumbnail = scrapedthumbnail
        plot = scrapertools.htmlclean(scrapedplot).strip()
        show = title
        logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))
        itemlist.append(Item(channel=item.channel, action="episodios", title=title, url=url, thumbnail=thumbnail + head,
                             plot=plot, show=show, fanart=thumbnail + head, viewmode="movies_with_plot",
                             context=renumbertools.context))

    pagina = scrapertools.find_single_match(data, '<li class=\'current\'>.*?</li><li><a href="([^"]+)"')

    if pagina:
        scrapedurl = pagina
        scrapedtitle = ">> Página Siguiente"
        scrapedthumbnail = ""
        scrapedplot = ""

        itemlist.append(Item(channel=item.channel, action="series", title=scrapedtitle, url=scrapedurl,
                             thumbnail=scrapedthumbnail, plot=scrapedplot, folder=True,
                             viewmode="movies_with_plot"))

    return itemlist


def episodios(item):
    logger.info()
    itemlist = []

    data = scrapertools.anti_cloudflare(item.url, headers=CHANNEL_DEFAULT_HEADERS, host=CHANNEL_HOST)
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;|<Br>|<BR>|<br>|<br/>|<br />|-\s", "", data)

    patron = "<p><span>(.*?)</span>"
    aux_plot = scrapertools.find_single_match(data, patron)

    patron = '<td><ahref="([^"]+)">(.*?)</a></td><td>(.*?)</td>'
    matches = re.compile(patron, re.DOTALL).findall(data)

    pelicula = False
    for scrapedurl, scrapedtitle, scrapeddate in matches:
        title = scrapedtitle.strip()  # scrapertools.unescape(scrapedtitle)
        url = scrapedurl
        thumbnail = item.thumbnail
        plot = aux_plot  # item.plot
        date = scrapeddate.strip()

        # TODO crear funcion que pasandole el titulo y buscando en un array de series establezca el valor el nombre
        # y temporada / capitulo para que funcione con trak.tv

        season = 1
        episode = 1
        patron = "Episodio\s+(\d+)"
        # logger.info("title {0}".format(title))
        # logger.info("patron {0}".format(patron))
        try:
            episode = scrapertools.get_match(title, patron)
            episode = int(episode)
            # logger.info("episode {0}".format(episode))
        except IndexError:
            pelicula = True
            pass
        except ValueError:
            pass

        if pelicula:
            title = "{0} ({1})".format(title, date)
            logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))
            item.url = url
            itemlist.append(Item(channel=item.channel, action="findvideos", title=title, url=url,
                                 thumbnail=thumbnail, plot=plot, fulltitle="{0} {1}".format(item.show, title),
                                 fanart=thumbnail, viewmode="movies_with_plot", folder=True))
        else:
            season, episode = renumbertools.numbered_for_tratk(item.channel, item.show, season, episode)

            title = "{0}x{1:02d} {2} ({3})".format(season, episode, "Episodio " + str(episode), date)

            logger.debug("title=[{0}], url=[{1}], thumbnail=[{2}]".format(title, url, thumbnail))

            itemlist.append(Item(channel=item.channel, action="findvideos", title=title, url=url,
                                 thumbnail=thumbnail, plot=plot, show=item.show, fulltitle="{0} {1}"
                                 .format(item.show, title), fanart=thumbnail, viewmode="movies_with_plot", folder=True))

    if config.get_library_support() and len(itemlist) > 0 and not pelicula:
        itemlist.append(Item(channel=item.channel, title="Añadir esta serie a la biblioteca de XBMC", url=item.url,
                             action="add_serie_to_library", extra="episodios", show=item.show))
        itemlist.append(Item(channel=item.channel, title="Descargar todos los episodios de la serie", url=item.url,
                             action="download_all_episodes", extra="episodios", show=item.show))

    elif config.get_library_support() and len(itemlist) == 1 and pelicula:
        itemlist.append(Item(channel=item.channel, action="add_pelicula_to_library", url=item.url,
                             title="Añadir película a la biblioteca", thumbnail=item.thumbnail,
                             fulltitle=item.fulltitle))

    return itemlist


def findvideos(item):
    logger.info()
    itemlist = []

    data = scrapertools.anti_cloudflare(item.url, headers=CHANNEL_DEFAULT_HEADERS, host=CHANNEL_HOST)
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;|<Br>|<BR>|<br>|<br/>|<br />|-\s", "", data)

    url_api = scrapertools.find_single_match(data, "http:\/\/api\.animeflv\.me\/[^\"]+")

    data = scrapertools.anti_cloudflare(url_api, headers=CHANNEL_DEFAULT_HEADERS)

    data = scrapertools.find_single_match(data, "var part = \[([^\]]+)")

    patron = '"([^"]+)"'
    matches = re.compile(patron, re.DOTALL).findall(data)

    list_quality = ["360", "480", "720", "1080"]

    # eliminamos la fecha del titulo a mostrar
    patron = "(.+?)\s\(\d{1,2}/\d{1,2}/\d{4}\)"
    title = scrapertools.find_single_match(item.title, patron)

    for _id, scrapedurl in enumerate(matches):
        itemlist.append(Item(channel=item.channel, action="play", url=scrapedurl, show=re.escape(item.show), fanart="",
                             title="Ver en calidad [{0}]".format(list_quality[_id]), thumbnail="", plot=item.plot,
                             folder=True, fulltitle=title, viewmode="movies_with_plot"))

    return sorted(itemlist, key=lambda it: int(scrapertools.find_single_match(it.title, "\[(.+?)\]")), reverse=True)


def get_cookie_value():
    cookies = os.path.join(config.get_data_path(), 'cookies', 'animeflv.me.dat')
    cookiedatafile = open(cookies, 'r')
    cookiedata = cookiedatafile.read()
    cookiedatafile.close()
    cfduid = scrapertools.find_single_match(cookiedata, "animeflv.*?__cfduid\s+([A-Za-z0-9\+\=]+)")
    cfduid = "__cfduid=" + cfduid + ";"
    cf_clearance = scrapertools.find_single_match(cookiedata, "animeflv.*?cf_clearance\s+([A-Za-z0-9\+\=\-]+)")
    cf_clearance = " cf_clearance=" + cf_clearance
    cookies_value = cfduid + cf_clearance

    return cookies_value
