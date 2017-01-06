# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canal (MetaSerie) por Hernan_Ar_c
# ------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from core import servertools


DEBUG = config.get_setting("debug")


def mainlist(item):
    logger.info("pelisalacarta.channels.metaserie mainlist")

    itemlist = []
    itemlist.append( Item(channel=item.channel, title="Series", action="todas", url="http://metaserie.com/series-agregadas", thumbnail='https://s32.postimg.org/544rx8n51/series.png', fanart='https://s32.postimg.org/544rx8n51/series.png'))
    itemlist.append( Item(channel=item.channel, title="Anime", action="todas", url="http://metaserie.com/animes-agregados",thumbnail='https://s31.postimg.org/lppob54d7/anime.png', fanart='https://s31.postimg.org/lppob54d7/anime.png'))
    itemlist.append( Item(channel=item.channel, title="Buscar", action="search", url="http://www.metaserie.com/?s=", thumbnail='https://s31.postimg.org/qose4p13f/Buscar.png', fanart='https://s31.postimg.org/qose4p13f/Buscar.png'))
    return itemlist

def todas(item):
    logger.info("pelisalacarta.channels.metaserie todas")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    
    patron = '<div class="poster">[^<]'
    patron +='<a href="([^"]+)" title="([^"]+)">[^<]'
    patron +='<div class="poster_efecto"><span>([^<]+)<.*?div>[^<]'
    patron +='<img.*?src="([^"]+)"'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle,scrapedplot, scrapedthumbnail in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapertools.decodeHtmlentities(scrapedtitle)
        #title = scrapedtitle.replace("&#8217;","'")
        thumbnail = scrapedthumbnail
        plot = scrapedplot
        fanart = 'https://s32.postimg.org/7g50yo39h/metaserie.png'
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="temporadas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart, contentSerieName=title))
    
    #Paginacion

    patron  = '<li><a class="next page-numbers local-link" href="([^"]+)">&raquo;.*?li>'
    next_page_url = scrapertools.find_single_match(data,'<li><a class="next page-numbers local-link" href="([^"]+)">&raquo;.*?li>')
    if next_page_url!="":
        import inspect
        itemlist.append(
            Item(
                channel = item.channel,
                action = "todas",
                title = ">> Página siguiente",
                url = next_page_url, thumbnail='https://s32.postimg.org/4zppxf5j9/siguiente.png'
            )
        )
    return itemlist

def temporadas(item):
    logger.debug("pelisalacarta.channels.metaserie temporadas")
    itemlist = []
    templist = []
    data = scrapertools.cache_page(item.url)
    
    patron = '<li class=".*?="([^"]+)".*?>([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapedtitle
        title = title.replace("&","x");
        thumbnail = item.thumbnail
        plot = item.plot
        fanart = scrapertools.find_single_match(data,'<img src="([^"]+)"/>.*?</a>')
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="episodios" , title=title ,fulltitle = item.title, url=url, thumbnail=thumbnail, plot=plot, fanart = fanart, contentSerieName=item.contentSerieName))
    
    if item.extra == 'temporadas':
        for tempitem in itemlist:
            templist += episodios(tempitem)
       
    if config.get_library_support() and len(itemlist) > 0:
        itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta serie a la biblioteca[/COLOR]', url=item.url,
                             action="add_serie_to_library", extra="temporadas", contentSerieName=item.contentSerieName))
    if item.extra == 'temporadas':
        return templist
    else:
        return itemlist
    

def episodios(item):
    logger.debug("pelisalacarta.channels.metaserie episodios")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    
    patron = '<td><h3 class=".*?href="([^"]+)".*?">([^<]+).*?td>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapedtitle
        title = title.replace ("&#215;","x")
        title = title.replace ("×","x")
        thumbnail = item.thumbnail
        plot = item.plot
        fanart=item.fanart
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="findvideos" , title=title, fulltitle=item.fulltitle, url=url, thumbnail=item.thumbnail, plot=plot, contentSerieName=item.contentSerieName))
        
    return itemlist

def search(item,texto):
    logger.info("metaserie.py search")
    texto = texto.replace(" ","+")
    item.url = item.url+texto
    itemlist = []
    if texto!='':
             try:
                 data = scrapertools.cache_page(item.url)
                 patron = '<a href="([^\"]+)" rel="bookmark" class="local-link">([^<]+)<.*?'
                 matches = re.compile(patron,re.DOTALL).findall(data)
                 scrapertools.printMatches(matches)
                 for scrapedurl,scrapedtitle in matches:
                     url = scrapedurl
                     title = scrapertools.decodeHtmlentities(scrapedtitle)
                     thumbnail = ''
                     plot = ''
                     if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
                     itemlist.append( Item(channel=item.channel, action="temporadas" , title=title , fulltitle=title, url=url, thumbnail=thumbnail, plot=plot, folder =True, contentSerieName=title ))

                 return itemlist
             except:
                import sys
                for line in sys.exc_info():
                    logger.error( "%s" % line )
             return []

   

def findvideos(item):
    logger.info ("pelisalacarta.channels.metaserie findvideos")
    itemlist=[]
    audio = {'la':'[COLOR limegreen]LATINO[/COLOR]','es':'[COLOR yellow]ESPAÑOL[/COLOR]','sub':'[COLOR red]ORIGINAL SUBTITULADO[/COLOR]'}
    data=scrapertools.cache_page(item.url)
    patron ='<td><img src="http:\/\/metaserie\.com\/wp-content\/themes\/mstheme\/gt\/assets\/img\/([^\.]+).png" width="20".*?<\/td>.*?<td><img src="http:\/\/www\.google\.com\/s2\/favicons\?domain=([^"]+)" \/>&nbsp;([^<]+)<\/td>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    
    anterior = scrapertools.find_single_match(data,'<th scope="col"><a href="([^"]+)" rel="prev" class="local-link">Anterior</a></th>')
    siguiente = scrapertools.find_single_match(data,'<th scope="col"><a href="([^"]+)" rel="next" class="local-link">Siguiente</a></th>')
    #titulo = scrapertools.find_single_match(data,'<h1 class="entry-title">([^<]+)</h1>		</header>')
    #titulo = titulo.encode('utf-8')

    for scrapedid, scrapedurl, scrapedserv in matches:
        url = scrapedurl
        title = item.title+' audio '+audio[scrapedid]+' en '+scrapedserv
        extra = item.thumbnail
        thumbnail = servertools.guess_server_thumbnail(scrapedserv)
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="play" , title=title, fulltitle=item.contentSerieName, url=url, thumbnail=thumbnail, extra=extra, folder= True))
    if item.extra1 != 'capitulos':
        if anterior !='':
            itemlist.append( Item(channel=item.channel, action="findvideos" , title='Capitulo Anterior' , url=anterior, thumbnail='https://s31.postimg.org/k5kpwyrgb/anterior.png', folder =True ))
        if siguiente !='':
            itemlist.append( Item(channel=item.channel, action="findvideos" , title='Capitulo Siguiente' , url=siguiente, thumbnail='https://s32.postimg.org/4zppxf5j9/siguiente.png', folder =True ))
    return itemlist

def play(item):
    logger.info("pelisalacarta.channels.metaserie play url="+item.url)
    itemlist =[]
    from core import servertools
    itemlist.extend(servertools.find_video_items(data=item.url))
    for videoitem in itemlist:
        video = item.channel
        videoitem.title = item.fulltitle
        videoitem.folder = False
        videoitem.thumbnail = item.extra
        videoitem.fulltitle = item.fulltitle
    return itemlist
   

    
