# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canal (cinecalidad) por Hernan_Ar_c
# ------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from core import servertools


DEBUG = config.get_setting("debug")
host=''
thumbmx='http://flags.fmcdn.net/data/flags/normal/mx.png'
thumbes='http://flags.fmcdn.net/data/flags/normal/es.png'
thumbbr='http://flags.fmcdn.net/data/flags/normal/br.png'


#def isGeneric():
#    return True

def mainlist(item):
    idioma2 ="destacadas" 
    logger.info("pelisalacarta.channels.cinecalidad mainlist")
    itemlist = []
    itemlist.append( Item(channel=item.channel, title="Audio Latino", action="submenu",host="http://cinecalidad.com/",thumbnail=thumbmx, extra = "peliculas"))
    itemlist.append( Item(channel=item.channel, title="Audio Castellano", action="submenu",host="http://cinecalidad.com/espana/",thumbnail=thumbes, extra = "peliculas"))
    itemlist.append( Item(channel=item.channel, title="Audio Portugues", action="submenu",host="http://cinemaqualidade.com/",thumbnail=thumbbr, extra ="filmes"))
    return itemlist


def submenu(item):
    idioma='peliculas'
    idioma2 ="destacada"
    host = item.host
    if item.host == "http://cinemaqualidade.com/" : 
       idioma = "filmes"
       idioma2 = "destacado"
    logger.info("pelisalacarta.channels.cinecalidad submenu")
    itemlist = []
    itemlist.append( Item(channel=item.channel, title=idioma.capitalize(), action="peliculas", url=host,thumbnail='https://s31.postimg.org/4g4lytrqj/peliculas.png', fanart='https://s31.postimg.org/4g4lytrqj/peliculas.png'))
    itemlist.append( Item(channel=item.channel, title="Destacadas", action="peliculas", url=host+"/genero-"+idioma+"/"+idioma2+"/", thumbnail='https://s32.postimg.org/wzyinepsl/destacadas.png', fanart='https://s32.postimg.org/wzyinepsl/destacadas.png'))
    itemlist.append( Item(channel=item.channel, title="Generos", action="generos", url=host+"/genero-"+idioma, thumbnail='https://s31.postimg.org/szbr0gmkb/generos.png',fanart='https://s31.postimg.org/szbr0gmkb/generos.png'))   
    itemlist.append( Item(channel=item.channel, title="Por Año", action="anyos", url=host+"/"+idioma+"-por-ano", thumbnail='https://s31.postimg.org/iyl5fvzqz/pora_o.png', fanart='https://s31.postimg.org/iyl5fvzqz/pora_o.png'))
    
    return itemlist



def anyos(item):
    logger.info("pelisalacarta.channels.cinecalidad generos")
    itemlist = []
    data = scrapertools.cache_page(item.url)
#   <a href="http://www.cinecalidad.com/peliculas/2016/">2016</a>    
    patron = '<a href="([^"]+)">([^<]+)</a> '
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapedtitle
#        title = title.replace("&","x");
        thumbnail = item.thumbnail
        plot = item.plot
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="peliculas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=item.thumbnail))

    return itemlist

def generos(item):
    tgenero = {"Comedia":"https://s32.postimg.org/q7g2qs90l/comedia.png",
               "Suspenso":"https://s31.postimg.org/kb629gscb/suspenso.png",
               "Drama":"https://s32.postimg.org/e6z83sqzp/drama.png",
               "Acción":"https://s32.postimg.org/4hp7gwh9x/accion.png",
               "Aventura":"https://s32.postimg.org/whwh56is5/aventura.png",
               "Romance":"https://s31.postimg.org/y7vai8dln/romance.png",
               "Fantas\xc3\xada":"https://s32.postimg.org/pklrf01id/fantasia.png",
               "Infantil":"https://s32.postimg.org/i53zwwgsl/infantil.png",
               "Ciencia ficción":"https://s32.postimg.org/6hp3tsxsl/ciencia_ficcion.png",
               "Terror":"https://s32.postimg.org/ca25xg0ed/terror.png",
               "Com\xc3\xa9dia":"https://s32.postimg.org/q7g2qs90l/comedia.png",
               "Suspense":"https://s31.postimg.org/kb629gscb/suspenso.png",
               "A\xc3\xa7\xc3\xa3o":"https://s32.postimg.org/4hp7gwh9x/accion.png",
               "Fantasia":"https://s32.postimg.org/pklrf01id/fantasia.png",
               "Fic\xc3\xa7\xc3\xa3o cient\xc3\xadfica":"https://s32.postimg.org/6hp3tsxsl/ciencia_ficcion.png"}
    logger.info("pelisalacarta.channels.cinecalidad generos")
    itemlist = []
    data = scrapertools.cache_page(item.url)
#             <li id="menu-item-2469" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2469"><a href="http://www.cinecalidad.com/genero-peliculas/comedia/">Comedia</a></li>    
    patron = '<li id="menu-item-.*?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><a href="([^"]+)">([^<]+)<\/a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapedtitle
#        title = title.replace("&","x");
        thumbnail = tgenero[scrapedtitle]
        plot = item.plot
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="peliculas" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=item.thumbnail))

    return itemlist

def peliculas(item):
    logger.info("pelisalacarta.channels.cinecalidad peliculas")
    itemlist = []
    data = scrapertools.cache_page(item.url)
   
    patron = '<div class="home_post_cont.*? post_box">.*?<a href="([^"]+)".*?src="([^"]+)".*?title="([^"]+)".*?p&gt;([^&]+)&lt;'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl,scrapedthumbnail,scrapedtitle,scrapedplot in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        title = scrapedtitle
        thumbnail = scrapedthumbnail
        plot = scrapedplot
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="findvideos" , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart='https://s31.postimg.org/puxmvsi7v/cinecalidad.png', contentTitle = title))
    
    try:     
        patron  = "<link rel='next' href='([^']+)' />" 
        next_page = re.compile(patron,re.DOTALL).findall(data)
        itemlist.append( Item(channel=item.channel, action="peliculas", title="Página siguiente >>" , url=next_page[0], fanart='https://s31.postimg.org/puxmvsi7v/cinecalidad.png') )

    except: pass
    return itemlist


def dec(item):
        link=[]
        val= item.split(' ')
        link = map(int, val)
        for i in range(len(link)):
            link[i] = link[i]-7
            real=''.join(map(chr, link))
        return (real)


def findvideos(item):
    servidor = {"http://uptobox.com/":"uptobox","http://userscloud.com/":"userscloud","https://my.pcloud.com/publink/show?code=":"pcloud","http://thevideos.tv/":"thevideos","http://ul.to/":"uploadedto","http://turbobit.net/":"turbobit","http://www.cinecalidad.com/protect/v.html?i=":"cinecalidad","http://www.mediafire.com/download/":"mediafire","https://www.youtube.com/watch?v=":"youtube","http://thevideos.tv/embed-":"thevideos","//www.youtube.com/embed/":"youtube","http://ok.ru/video/":"okru","http://ok.ru/videoembed/":"okru","http://www.cinemaqualidade.com/protect/v.html?i=":"cinemaqualidade.com","http://usersfiles.com/":"usersfiles","https://depositfiles.com/files/":"depositfiles","http://www.nowvideo.sx/video/":"nowvideo","http://vidbull.com/":"vidbull"}
    logger.info("pelisalacarta.channels.cinecalidad links")
    itemlist=[]
    data = scrapertools.cache_page(item.url)
    
#   {h=dec("111 123 123 119 65 54 54 124 119 123 118 105 118 127 53 106 118 116 54")+dec("114 114 110 115 110 55 121 117 64 120 120 115");}    
    patron = 'dec\("([^"]+)"\)\+dec\("([^"]+)"\)'
    matches = re.compile(patron,re.DOTALL).findall(data)
    recomendados = ["uptobox","thevideos","nowvideo","pcloud"]
    for scrapedurl,scrapedtitle in matches:
        if dec(scrapedurl) in servidor: 
           url = dec(scrapedurl)+dec(scrapedtitle)
           title = "Ver "+item.contentTitle+" en "+servidor[dec(scrapedurl)].upper()
           if (servidor[dec(scrapedurl)]) in recomendados:
              title=title+"[COLOR limegreen] [I] (Recomedado) [/I] [/COLOR]"
#           if (servidor[dec(scrapedurl)])=='pcloud':
#              thumbnail='https://pbs.twimg.com/profile_images/687592526694473728/bCQCZC7b.png'
#           else:
           thumbnail = servertools.guess_server_thumbnail(servidor[dec(scrapedurl)])
           plot = ""
           if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
           itemlist.append( Item(channel=item.channel, action="play" , title=title ,fulltitle = item.title, url=url, thumbnail=thumbnail, plot=plot,extra=item.thumbnail, server=servidor[dec(scrapedurl)]))
    
    if config.get_library_support() and len(itemlist) > 0 and item.extra !='findvideos' :
        itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta pelicula a la biblioteca[/COLOR]', url=item.url,
                             action="add_pelicula_to_library", extra="findvideos", contentTitle = item.contentTitle))
    return itemlist

def play(item):
    
    logger.info("pelisalacarta.channels.cinecalidad play url="+item.url)
    itemlist = servertools.find_video_items(data=item.url)
            
    for videoitem in itemlist:
        videoitem.title = item.fulltitle
        videoitem.fulltitle = item.fulltitle
        videoitem.thumbnail = item.extra
        videochannel=item.channel
    return itemlist

