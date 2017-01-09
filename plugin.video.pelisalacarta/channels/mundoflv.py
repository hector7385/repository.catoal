# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canal (mundoflv) por Hernan_Ar_c
# ------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from core import servertools


DEBUG = config.get_setting("debug")
host="http://mundoflv.com"
thumbmx ='http://flags.fmcdn.net/data/flags/normal/mx.png'
thumbes ='http://flags.fmcdn.net/data/flags/normal/es.png'
thumben ='http://flags.fmcdn.net/data/flags/normal/gb.png'
thumbsub ='https://s32.postimg.org/nzstk8z11/sub.png'

def isGeneric():
    return True

def mainlist(item):
    logger.info("pelisalacarta.channels.mundoflv mainlist")

    itemlist = []
    
    itemlist.append( Item(channel=item.channel, title="Series", action="todas", url=host, thumbnail='https://s32.postimg.org/544rx8n51/series.png', fanart='https://s32.postimg.org/544rx8n51/series.png'))
    
    itemlist.append( Item(channel=item.channel, title="Alfabetico", action="letras", url=host, thumbnail='https://s31.postimg.org/c3bm9cnl7/a_z.png', fanart='https://s31.postimg.org/c3bm9cnl7/a_z.png'))
    
    itemlist.append( Item(channel=item.channel, title="Mas vistas", action="masvistas", url=host, thumbnail='https://s32.postimg.org/466gt3ipx/vistas.png', fanart='https://s32.postimg.org/466gt3ipx/vistas.png'))
    
    itemlist.append( Item(channel=item.channel, title="Recomendadas", action="recomendadas", url=host, thumbnail='https://s31.postimg.org/4bsjyc4iz/recomendadas.png', fanart='https://s31.postimg.org/4bsjyc4iz/recomendadas.png'))
    
    itemlist.append( Item(channel=item.channel, title="Ultimas Agregadas", action="ultimas", url=host, thumbnail='https://s31.postimg.org/3ua9kwg23/ultimas.png', fanart='https://s31.postimg.org/3ua9kwg23/ultimas.png'))

    itemlist.append( Item(channel=item.channel, title="Buscar", action="search", url='http://mundoflv.com/?s=', thumbnail='https://s31.postimg.org/qose4p13f/Buscar.png', fanart='https://s31.postimg.org/qose4p13f/Buscar.png'))

    return itemlist


def todas(item):
    logger.info("pelisalacarta.channels.mundoflv todas")
    itemlist = []
    data = scrapertools.cache_page(item.url)

    '''<a href="http://mundoflv.com/jessica-jones/" title="Jessica Jones (2015)">
<div class="img">
<img src="http://mundoflv.com/wp-content/uploads/2015/11/jessica-203x300.jpg" alt="Jessica Jones ()" />'''

    patron = '<a href="([^"]+)" title="([^"]+)">.*?'
    patron +='<div class="img">.*?'
    patron +='<img src="([^"]+)" alt.*?>'
    
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle, scrapedthumbnail in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapertools.decodeHtmlentities(scrapedtitle)
        thumbnail = scrapedthumbnail
        plot = ''
        fanart = 'https://s32.postimg.org/h1ewz9hhx/mundoflv.png'
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="idioma" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart, contentSerieName=title))
    
    #Paginacion

    patron  = '<link rel="next" href="([^"]+)" />'
    next_page_url = scrapertools.find_single_match(data,'<link rel="next" href="([^"]+)" />')
    if next_page_url!="":
        import inspect
        itemlist.append(
            Item(
                channel = item.channel,
                action = "todas",
                title = ">> Página siguiente",
                url = next_page_url
            )
        )
    return itemlist


def letras(item):

    thumbletras = {'0-9':'https://s32.postimg.org/drojt686d/image.png','0 - 9':'https://s32.postimg.org/drojt686d/image.png','#':'https://s32.postimg.org/drojt686d/image.png','a':'https://s32.postimg.org/llp5ekfz9/image.png','b':'https://s32.postimg.org/y1qgm1yp1/image.png','c':'https://s32.postimg.org/vlon87gmd/image.png','d':'https://s32.postimg.org/3zlvnix9h/image.png','e':'https://s32.postimg.org/bgv32qmsl/image.png','f':'https://s32.postimg.org/y6u7vq605/image.png','g':'https://s32.postimg.org/9237ib6jp/image.png','h':'https://s32.postimg.org/812yt6pk5/image.png','i':'https://s32.postimg.org/6nbbxvqat/image.png','j':'https://s32.postimg.org/axpztgvdx/image.png','k':'https://s32.postimg.org/976yrzdut/image.png','l':'https://s32.postimg.org/fmal2e9yd/image.png','m':'https://s32.postimg.org/m19lz2go5/image.png','n':'https://s32.postimg.org/b2ycgvs2t/image.png','o':'https://s32.postimg.org/c6igsucpx/image.png','p':'https://s32.postimg.org/jnro82291/image.png','q':'https://s32.postimg.org/ve5lpfv1h/image.png','r':'https://s32.postimg.org/nmovqvqw5/image.png','s':'https://s32.postimg.org/zd2t89jol/image.png','t':'https://s32.postimg.org/wk9lo8jc5/image.png','u':'https://s32.postimg.org/w8s5bh2w5/image.png','v':'https://s32.postimg.org/e7dlrey91/image.png','w':'https://s32.postimg.org/fnp49k15x/image.png','x':'https://s32.postimg.org/dkep1w1d1/image.png','y':'https://s32.postimg.org/um7j3zg85/image.png','z':'https://s32.postimg.org/jb4vfm9d1/image.png'}

    logger.info("pelisalacarta.channels.mundoflv letras")
    itemlist = []
    data = scrapertools.cache_page(item.url)

    patron = '<li><a.*?href="([^"]+)">([^<]+)<\/a><\/li>'
    # patron = '<li class=".*?="([^"]+)".*?>([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapedtitle
        if scrapedtitle.lower() in thumbletras:
           thumbnail = thumbletras[scrapedtitle.lower()]
        else:
            thumbnail = ''
        plot = ""
        fanart = item.fanart
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="todas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart ,contentSerieName=title))

    return itemlist

def masvistas(item):
    logger.info("pelisalacarta.channels.mundoflv masvistas")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    realplot=''
    patron = '<li> <A HREF="([^"]+)"> <.*?>Ver ([^<]+)</A></li>'
    # patron = '<li class=".*?="([^"]+)".*?>([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        data = scrapertools.cache_page(scrapedurl)
        thumbnail= scrapertools.get_match(data,'<meta property="og:image" content="([^"]+)" />')
        realplot = scrapertools.find_single_match(data, '\/><\/a>([^*]+)<p><\/p>.*')
        plot = scrapertools.remove_htmltags(realplot)
        title = scrapedtitle.replace('online','')
        title = scrapertools.decodeHtmlentities(title)
        # title = title.replace("&","x");
        fanart = item.fanart
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="temporadas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart, contentSerieName=title))

    return itemlist

def recomendadas(item):
    logger.info("pelisalacarta.channels.mundoflv masvistas")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    realplot=''
    patron = '<li><A HREF="([^"]+)"><.*?>Ver ([^<]+)<\/A><\/li>'
    # patron = '<li class=".*?="([^"]+)".*?>([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        data = scrapertools.cache_page(scrapedurl)
        thumbnail= scrapertools.get_match(data,'<meta property="og:image" content="([^"]+)" />')
        realplot = scrapertools.find_single_match(data, '\/><\/a>([^*]+)<p><\/p>.*')
        plot = scrapertools.remove_htmltags(realplot)
        title = scrapedtitle.replace('online','')
        title = title = scrapertools.decodeHtmlentities(title) 
        # title = title.replace("&","x");
        fanart = item.fanart
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="temporadas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart,contentSerieName=title))

    return itemlist

def ultimas(item):
    logger.info("pelisalacarta.channels.mundoflv masvistas")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    realplot=''
    patron = '<li><A HREF="([^"]+)"> <.*?>Ver ([^<]+)<\/A><\/li>'
    # patron = '<li class=".*?="([^"]+)".*?>([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        data = scrapertools.cache_page(scrapedurl)
        thumbnail= scrapertools.get_match(data,'<meta property="og:image" content="([^"]+)" />')
        realplot = scrapertools.find_single_match(data, '\/><\/a>([^*]+)<p><\/p>.*')
        plot = scrapertools.remove_htmltags(realplot)
        plot = ""
        title = scrapedtitle.replace('online','')
        title = scrapertools.decodeHtmlentities(title)
        # title = title.replace("&","x");
        fanart = item.fanart
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="temporadas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart,contentSerieName=title))

    return itemlist

def temporadas(item):
    logger.debug("pelisalacarta.channels.mundoflv temporadas")
    
    itemlist = []
    templist = []
    data = scrapertools.cache_page(item.url)
    realplot = ''
    patron = "<button class='classnamer' onclick='javascript: mostrarcapitulos.*?blank'>([^<]+)</button>"
    
    matches = re.compile(patron,re.DOTALL).findall(data)
    
    serieid = scrapertools.find_single_match(data,"<link rel='shortlink' href='http:\/\/mundoflv.com\/\?p=([^']+)' \/>")
    item.thumbnail = item.thumbvid
    for scrapedtitle in matches:
        url = 'http://mundoflv.com/wp-content/themes/wpRafael/includes/capitulos.php?serie='+serieid+'&sr=&temporada=' + scrapedtitle
        title = 'Temporada '+ scrapertools.decodeHtmlentities(scrapedtitle)
        thumbnail = item.thumbnail
        realplot = scrapertools.find_single_match(data, '\/><\/a>([^*]+)<p><\/p>.*')
        plot = scrapertools.remove_htmltags(realplot)
        fanart = ''#scrapertools.find_single_match(data,'<img src="([^"]+)"/>.*?</a>')
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="episodios" , title=title , fulltitle=item.title, url=url, thumbnail=thumbnail, plot=plot, fanart = fanart, extra1=item.extra1, contentSerieName=item.contentSerieName))
    
    if item.extra=='temporadas':
        for tempitem in itemlist:
    	    templist += episodios(tempitem)
        
    if config.get_library_support() and len(itemlist) > 0:
        itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta serie a la biblioteca[/COLOR]', url=item.url,
                             action="add_serie_to_library", extra="temporadas", contentSerieName=item.contentSerieName, extra1 = item.extra1))
    if item.extra=='temporadas':
    	return templist
    else:
    	return itemlist

def episodios(item):
    logger.debug("pelisalacarta.channels.mundoflv episodios")
    itemlist = []
    data = scrapertools.cache_page(item.url)
     
    patron = "<button class='classnamer' onclick='javascript: mostrarenlaces\(([^\)]+)\).*?<"
    matches = re.compile(patron,re.DOTALL).findall(data)
    
    for scrapedtitle in matches:
        item.url=item.url.replace("&sr","")
        item.url=item.url.replace("capitulos","enlaces")
        url = item.url+'&capitulo=' + scrapedtitle
        title=item.contentSerieName+' '+item.title.strip('Temporada')+'x'+scrapedtitle
        thumbnail = item.thumbnail
        plot = item.plot
        fanart=''
        idioma=''
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="findvideos" , title=title, fulltitle=item.fulltitle, url=url, thumbnail=item.thumbnail, plot=plot, extra1=item.extra1,idioma=''))
    
    return itemlist
    
def idioma(item):
    logger.info("pelisalacarta.channels.mundoflv idioma")

    itemlist = []
    thumbvid =item.thumbnail
    itemlist.append( Item(channel=item.channel, title="Latino", action="temporadas", url=item.url, thumbnail=thumbmx, fanart='', extra1 = 'la', fulltitle = item.title, thumbvid = thumbvid, contentSerieName=item.contentSerieName))
    
    itemlist.append( Item(channel=item.channel, title="Español", action="temporadas", url=item.url, thumbnail=thumbes, fanart='', extra1 = 'es', fulltitle = item.title, thumbvid = thumbvid, contentSerieName=item.contentSerieName))
    
    itemlist.append( Item(channel=item.channel, title="Subtitulado", action="temporadas", url=item.url, thumbnail=thumbsub, fanart='', extra1 = 'sub', fulltitle = item.title, thumbvid = thumbvid, contentSerieName=item.contentSerieName))
    
    itemlist.append( Item(channel=item.channel, title="Original", action="temporadas", url=item.url, thumbnail=thumben, fanart='', extra1 = 'en', fulltitle = item.title, thumbvid = thumbvid, contentSerieName=item.contentSerieName))
    
    return itemlist 

def findvideos(item):

    logger.info("pelisalacarta.channels.mundoflv findvideos")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    
    patron ='href="([^"]+)".*?'
    patron +='color="gold">([^<]+)<'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl, scrapedidioma in matches:
        if scrapedidioma == item.extra1:
           url = scrapedurl
           data = scrapertools.cache_page(url)
           from core import servertools
           itemlist.extend(servertools.find_video_items(item=item, data=data))
    for videoitem in itemlist:
        videoitem.channel = item.channel
        videoitem.folder = False
        videoitem.extra = item.thumbvid
        videoitem.fulltitle = item.fulltitle
#        videoitem.action = play
    return itemlist

def busqueda(item):
    logger.info("mundoflv.py busqueda")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    patron = '<img class=.*?src="([^"]+)" alt="([^"]+)">.<span><\/span>.<\/div>.<div.*?>.<!--.*?>.<span class.*?>.<span class.*?\/span>.<\/span>.<!--.*?>.<h3><a href="([^"]+)">.*?/h3>'
   #patron +='.*?<h3><a href="([^"]+)"</a></h3>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)
    
    for scrapedthumbnail, scrapedtitle, scrapedurl in matches:
        url = scrapedurl
        title = scrapertools.decodeHtmlentities(scrapedtitle)
        thumbnail = scrapedthumbnail
        plot = ''
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="idioma" , title=title , fulltitle=title, url=url, thumbnail=thumbnail, plot=plot, contentSerieName=title))
   #Paginacion
    patron  = "<a rel='nofollow' class=previouspostslink' href='([^']+)'>Siguiente &rsaquo;</a>"
    next_page_url = scrapertools.find_single_match(data,"<a rel='nofollow' class=previouspostslink' href='([^']+)'>Siguiente &rsaquo;</a>")
    if next_page_url!="":
        item.url=next_page_url
        import inspect
        itemlist.append(Item(channel = item.channel,action = "busqueda",title = ">> Página siguiente", url = next_page_url))   

    return itemlist

def search(item,texto):
    logger.info("mundoflv.py search")
    texto = texto.replace(" ","+")
    item.url = item.url+texto
    if texto!='':
       return busqueda(item)    

