# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para PrivateHD
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import os
from core import logger
from core import config
from core import scrapertools
from core import servertools
from core.item import Item

__channel__ = "privatehd"


DEBUG = config.get_setting("debug")


def mainlist(item):
    logger.info("deportesalacarta.channels.privatehd mainlist")
    itemlist = []

    paises = [["Polonia", "pol"], ["Inglaterra", "uk"], ["Holanda", "nl"], ["Francia", "fr"], ["Alemania", "de"], ["España", "es"], ["Portugal", "por"], ["Resto del mundo", "rm"]]
    data = scrapertools.downloadpage("http://privatehd.pw/live.php")
    patron = '<li><input type="button".*?Enviar\(\'([^\']+)\''
    matches = scrapertools.find_multiple_matches(data, patron)
    for i, url in enumerate(matches):
        scrapedtitle = "[COLOR green]"+paises[i][0]+"[/COLOR]"
        scrapedthumbnail = "http://privatehd.pw/img/"+paises[i][1]+".png"
        url = "http://privatehd.pw/"+url
        itemlist.append(item.clone(title=scrapedtitle, action="canales", url=url, thumbnail=scrapedthumbnail))

    return itemlist


def canales(item):
    logger.info("deportesalacarta.channels.privatehd canales")
    itemlist = []
    
    data = scrapertools.downloadpage(item.url)
    patron = '<li><a href=\'([^\']+)\'.*?<td.*?>([^<]+)</td>.*?src="([^"]+)"'
    matches = scrapertools.find_multiple_matches(data, patron)
    for scrapedurl, scrapedtitle, scrapedthumbnail  in matches:
        scrapedurl = "http://privatehd.pw/"+scrapedurl.rsplit("&name", 1)[0]
        scrapedthumbnail = "http://privatehd.pw/"+scrapedthumbnail
        itemlist.append(item.clone(title=scrapedtitle, action="play", url=scrapedurl, thumbnail=scrapedthumbnail))
    
    return itemlist


def play(item):
    logger.info("deportesalacarta.privatehd go")
    itemlist = []

    headers = [["User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"]]
    fulltitle = item.title
    data = scrapertools.cachePage(item.url)
    iframe = scrapertools.find_single_match(data, '<center><iframe.*?src="(http://privatehd.pw/tv[^"]+)"')
    data = scrapertools.cachePage(iframe)

    urls = servertools.findvideosbyserver(data, "p2p")
    if urls:
        url = urls[0][1] + "|" + fulltitle
        itemlist.append(Item(channel=__channel__, title=item.title, server="p2p", url=url, action="play", folder=False))
    else:
        headers.append(["Referer", iframe])
        newurl = scrapertools.find_single_match(data, "src='(http://privatehd.pw/server[^']+)'")
        newurl = newurl.replace("channel.php?file=", "embed.php?a=") + "&strech="
        data = scrapertools.downloadpage(newurl, headers=headers)

        url_video = scrapertools.find_single_match(data, "'streamer'\s*,\s*'([^']+)'")
        if "rtmp" in url_video:
            file = scrapertools.find_single_match(data, "'file'\s*,\s*'([^']+)'")
            url_video += " playpath=%s swfUrl=http://privatehd.pw/player.swf live=true swfVfy=1 pageUrl=%s token=0fea41113b03061a" % (file, newurl)

        itemlist.append(Item(channel=__channel__, title=item.title, server="directo", url=url_video, action="play", folder=False))
    
    return itemlist
