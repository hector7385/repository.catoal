# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para MotoGPEnNegro
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import base64, urllib, urlparse
from core import logger
from core import config
from core import scrapertools
from core.item import Item

__channel__ = "motogpennegro"

DEBUG = config.get_setting("debug")


def mainlist(item):
    logger.info("deportesalacarta.channels.motogpennegro mainlist")
    itemlist = []

    data = scrapertools.cachePage("https://motogpennegro.wordpress.com/streaming/")
    patron = '<a href="(http://adf.ly/[^"]+)".*?src="(.*?(?:jpg|png)).*?alt="([^"]+)"'
    matches = scrapertools.find_multiple_matches(data, patron)
    for scrapedurl, scrapedthumbnail, tipo in matches:
        if tipo == "MotoGPFlash":
            title = "[COLOR darkred]Canal Moto GP (Flash)[/COLOR]"
            fanart = "http://i.imgur.com/eN4utvy.jpg?1"
            action = "play_flash"
            id = 1
        elif "MotoGP" in tipo:
            title = "[COLOR darkred]Canal Moto GP (Acestream)[/COLOR]"
            fanart = "http://i.imgur.com/eN4utvy.jpg?1"
            action = "play"
            id = 0
        elif "F1" in tipo: 
            title = "[COLOR darkcyan]Canal Formula 1 (Acestream)[/COLOR]"
            fanart = "http://i.imgur.com/pdnifhG.jpg?1"
            action = "play"
            id = 2

        itemlist.append(Item(channel=__channel__, title=title, url=scrapedurl, action=action, thumbnail=scrapedthumbnail, fanart=fanart, order=id, folder=False))
    itemlist.sort(key=lambda item:item.order)
    itemlist.append(Item(channel=__channel__, title="[COLOR sienna]Hemeroteca (Solo 1fichier)[/COLOR]", url="", action="hemeroteca", thumbnail="http://i.imgur.com/LjJu39J.png?1", fanart="http://i.imgur.com/eN4utvy.jpg?1"))

    return itemlist


def hemeroteca(item):
    logger.info("deportesalacarta.channels.motogpennegro hemeroteca")
    itemlist = []

    title = "[COLOR goldenrod]%s[/COLOR]"
    itemlist.append(Item(channel=__channel__, title=title % "Temporada 2016", url="https://motogpennegro.wordpress.com/videoclub/temporada2016/", action="menu_heme", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Temporada 2015", url="https://motogpennegro.wordpress.com/videoclub/carrerashistoricas/los10s/temporada2015/", action="menu_heme", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Temporada 2014", url="https://motogpennegro.wordpress.com/videoclub/carrerashistoricas/los10s/temporada2014/", action="menu_heme", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Temporada 2013", url="https://1fichier.com/dir/EW6eYIUF", action="findvideos", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Temporada 2010", url="https://1fichier.com/dir/r1qZyW62", action="findvideos", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Los 80", url="https://motogpennegro.wordpress.com/videoclub/carrerashistoricas/los80s/", action="historico", thumbnail="https://motogpennegro.files.wordpress.com/2016/05/back-to-80s-e1463507114603.png", fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Los 70", url="https://motogpennegro.wordpress.com/videoclub/carrerashistoricas/los70s/", action="historico", thumbnail="https://motogpennegro.files.wordpress.com/2015/07/0_main-741.jpg", fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Documentales", url="https://1fichier.com/dir/gDKDZGYg", action="findvideos", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))
    itemlist.append(Item(channel=__channel__, title=title % "Extras", url="https://1fichier.com/dir/6B01q5z2", action="findvideos", thumbnail=item.thumbnail, fanart=item.fanart, folder=True))

    return itemlist


def menu_heme(item):
    logger.info("deportesalacarta.channels.motogpennegro menu_heme")
    itemlist = []
    data = scrapertools.cachePage(item.url)

    bloque = scrapertools.find_single_match(data, '<div class="entry-content">(.*?)<footer class="entry-meta">')
    matches = scrapertools.find_multiple_matches(bloque, 'alt="([^"]+)"   /></h4>.*?href="([^"]+)".*?src="([^"]+)"')
    for scrapedtitle, scrapedurl, scrapedthumbnail in matches:
        if "facebook" in scrapedurl: continue
        scrapedtitle = "[COLOR orangered]"+scrapertools.decodeHtmlentities(scrapedtitle)+"[/COLOR]"
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="carreras", thumbnail=scrapedthumbnail, fanart=item.fanart, folder=True))
    
    return itemlist


def carreras(item):
    logger.info("deportesalacarta.channels.motogpennegro carreras")
    itemlist = []
    data = scrapertools.cachePage(item.url)

    bloque = scrapertools.find_single_match(data, '(INSTRUCCIONES DE DESCARGA.*?<footer class="entry-meta">)')
    if "GALA" in item.title:
        matches = scrapertools.find_multiple_matches(bloque, '<img class="  wp-image.*?src="([^"]+)".*?href="(http://adf.ly/[^"]+)"')
        for scrapedurl in matches:
            scrapedtitle = "[COLOR darkorange]"+item.title+"   [1fichier][/COLOR]"
            itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="play", thumbnail=item.thumbnail, fanart=item.fanart, folder=False))
    if len(itemlist) == 0:
        patron = '(?:<h2|<h3) style="text-align:center;"><span[^>]+>([\w\s]+)<.*?href="(http://adf.ly/[^"]+)"'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedtitle, scrapedurl in matches:
            scrapedtitle = "[COLOR green]Ver Carrera de[/COLOR] [COLOR darkorange]"+scrapedtitle+"   [1fichier][/COLOR]"
            itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="play", thumbnail=item.thumbnail, fanart=item.fanart, folder=False))
        
        itemlist.reverse()

    return itemlist


def historico(item):
    logger.info("deportesalacarta.channels.motogpennegro historico")
    itemlist = []
    data = scrapertools.cachePage(item.url)

    bloque = scrapertools.find_single_match(data, '<div class="entry-content">(.*?)<footer class="entry-meta">')
    matches = scrapertools.find_multiple_matches(bloque, 'alt="19([^"]+)".*?href="([^"]+)".*?src="([^"]+)"')
    for scrapedtitle, scrapedurl, scrapedthumbnail in matches:
        if "facebook" in scrapedurl: continue
        scrapedtitle = "[COLOR orangered]Año 19"+scrapertools.decodeHtmlentities(scrapedtitle)+"[/COLOR]"
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="findvideos", thumbnail=scrapedthumbnail, fanart=item.fanart, folder=True))
    
    return itemlist


def findvideos(item):
    logger.info("deportesalacarta.channels.motogpennegro findvideos")
    itemlist = []
    if "adf.ly" in item.url:
        data = scrapertools.cachePage(item.url)
        item.url = decode_adfly(data)
    data = scrapertools.cachePage(item.url)

    patron = '<tr>.*?<a href="([^"]+)".*?>(.*?)</a>.*?<td class="normal">(.*?)</td>'
    matches = scrapertools.find_multiple_matches(data, patron)
    for scrapedurl, scrapedtitle, size in matches:
        scrapedtitle = "[COLOR sienna]"+scrapedtitle+"[/COLOR]  [COLOR orangered]("+size+")   [1fichier][/COLOR]"
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="play", thumbnail=item.thumbnail, fanart=item.fanart, folder=False))
    return itemlist
    
    
def play(item):
    logger.info("deportesalacarta.channels.motogpennegro play")
    itemlist = []
    data = scrapertools.cachePage(item.url)
    if "Acestream" in item.title:
        decoded_url = decode_adfly(data)
        url = "acestream://" + decoded_url.rsplit("/",1)[1] + "|" + item.title
        itemlist.append(Item(channel=__channel__, title=item.title, action="play", server="p2p", url=url, thumbnail=item.thumbnail, folder=False))
    elif "1fichier" in item.url:
        itemlist.append(Item(channel=__channel__, title=item.title, action="play", server="onefichier", url=item.url, thumbnail=item.thumbnail, folder=False))
    else:
        url = decode_adfly(data)
        itemlist.append(Item(channel=__channel__, title=item.title, action="play", server="onefichier", url=url, thumbnail=item.thumbnail, folder=False))
    return itemlist


def play_flash(item):
    logger.info("deportesalacarta.channels.motogpennegro play_flash")
    data = scrapertools.cachePage(item.url)
    url = decode_adfly(data)
    data = scrapertools.downloadpage(url)
    url_flash = scrapertools.find_single_match(data, 'src="(http://www.sunhd.info/[^"]+)"')
    host = urlparse.urljoin(url, '/')
    url = "catcher=%s&url=%s&referer=%s" % ("streams", url_flash, host)
    import xbmc
    xbmc.executebuiltin("XBMC.RunPlugin(plugin://plugin.video.SportsDevil/?item=%s&mode=1)" % urllib.quote_plus(url))


def decode_adfly(data):
    ysmm = scrapertools.find_single_match(data, "var ysmm = '([^']+)'")
    left = ''
    right = ''
    for c in [ysmm[i:i+2] for i in range(0, len(ysmm), 2)]:
        left += c[0]
        right = c[1] + right

    decoded_url = base64.b64decode(left.encode() + right.encode())[2:].decode()
    return decoded_url
