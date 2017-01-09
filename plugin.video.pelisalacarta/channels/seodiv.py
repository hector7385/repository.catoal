# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canal (seodiv) por Hernan_Ar_c
# ------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os, sys


from core import logger
from core import config
from core import scrapertools
from core.item import Item
from core import servertools


DEBUG = config.get_setting("debug")

host='http://www.seodiv.com'


def mainlist(item):
    logger.info("pelisalacarta.channels.seodiv mainlist")

    itemlist = []
    

    itemlist.append( Item(channel=item.channel, title="Todos", action="todas", url=host,thumbnail='https://s32.postimg.org/544rx8n51/series.png', fanart='https://s32.postimg.org/544rx8n51/series.png'))
   
    return itemlist

def todas(item):

    logger.info("pelisalacarta.channels.seodiv todas")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    
    patron ='<\/div><img src="([^"]+)".*?\/>.*?'
    patron+='<div class="title-topic">([^<]+)<\/div>.*?'
    patron +='<div class="sh-topic">([^<]+)<\/div><\/a>.*?'
    patron +='<div class="read-more-top"><a href="([^"]+)" style='
       
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedthumbnail, scrapedtitle, scrapedplot, scrapedurl in matches: 
        url = host+scrapedurl
        title = scrapedtitle.decode('utf-8')
        thumbnail = scrapedthumbnail
        fanart = 'https://s32.postimg.org/gh8lhbkb9/seodiv.png'
        plot = scrapedplot
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="temporadas" ,title=title , url=url, thumbnail=thumbnail, fanart=fanart, plot= plot, contentSerieName=title, extra=''))
           

    return itemlist

    
def categorias(item):
    logger.info("pelisalacarta.channels.seodiv categoias")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    patron ="<a href='([^']+)' class='tag-link-.*? tag-link-position-.*?' title='.*?' style='font-size: 11px;'>([^<]+)<\/a>" 
    
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle in matches:
	url = scrapedurl
	title = scrapedtitle
	if (DEBUG): logger.info("title=["+title+"], url=["+url+"])")
	itemlist.append( Item(channel=item.channel, action="todas" , title=title, fulltitle=item.fulltitle, url=url))
        
    return itemlist            
        
def temporadas(item):
    logger.info("pelisalacarta.channels.seodiv temporadas")
    itemlist = []
    templist = []
    data = scrapertools.cache_page(item.url)
    url_base= item.url
    patron = '<a class="collapsed" data-toggle="collapse" data-parent="#accordion" href=.*? aria-expanded="false" aria-controls=.*?>([^<]+)<\/a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    temp=1
    if 'Temporada'in str(matches):
      	for scrapedtitle in matches:
           url = url_base
           tempo = re.findall(r'\d+',scrapedtitle)
           if tempo:
              title ='Temporada'+' '+ tempo[0]
           else:
              title = scrapedtitle.lower()
           thumbnail = item.thumbnail
           plot = item.plot
           fanart = scrapertools.find_single_match(data,'<img src="([^"]+)"/>.*?</a>')
           if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
           itemlist.append( Item(channel=item.channel, action="episodios" , title=title , fulltitle=item.title, url=url, thumbnail=thumbnail, plot=plot, fanart = fanart, temp=str(temp),contentSerieName=item.contentSerieName))
           temp = temp+1
        if item.extra=='temporadas':
           for tempitem in itemlist:
              templist += episodios(tempitem)
        if config.get_library_support() and len(itemlist) > 0:
           itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta serie a la biblioteca[/COLOR]', url=item.url,
                             action="add_serie_to_library", extra="temporadas", contentSerieName=item.contentSerieName, extra1 = item.extra1, temp=str(temp)))
        if item.extra=='temporadas':
            return templist
        else:
            return itemlist
    else:
        itemlist=episodios(item)
        if config.get_library_support() and len(itemlist) > 0:
           itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta serie a la biblioteca[/COLOR]', url=item.url,
                             action="add_serie_to_library", extra="temporadas", contentSerieName=item.contentSerieName, extra1 = item.extra1, temp=str(temp)))
        return itemlist

def episodios(item):
    
    logger.debug("pelisalacarta.channels.seodiv episodios")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    tempo = item.title
    if 'Temporada'in item.title:
        item.title = item.title.replace('Temporada', 'temporada')
        item.title = item.title.strip()
        item.title = item.title.replace(' ','-')
                
    #patron ='<li><a href="([^"]+)">.*?Capitulo.*?([\d\d<]+)<'
    patron ='<li><a href="([^"]+)">.*?(Capitulo|Pelicula).*?([\d]+)'
        
    matches = re.compile(patron,re.DOTALL).findall(data)
    idioma = scrapertools.find_single_match(data,' <p><span class="ah-lead-tit">Idioma:</span>&nbsp;<span id="l-vipusk">([^<]+)</span></p>')
    #if item.temp =='': item.temp='1'
    for scrapedurl, scrapedtipo, scrapedtitle in matches:
        url = host+scrapedurl
    #    title = item.contentSerieName+' '+item.temp+'x'+scrapedtitle+' ('+idioma+')'
        title =''
        thumbnail = item.thumbnail
        plot = item.plot
        fanart=''

        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        if 'temporada' in item.title and item.title in scrapedurl and scrapedtipo =='Capitulo' and item.temp !='':
            title = item.contentSerieName+' '+item.temp+'x'+scrapedtitle+' ('+idioma+')'
            itemlist.append( Item(channel=item.channel, action="findvideos" , title=title, fulltitle=item.fulltitle, url=url, thumbnail=item.thumbnail, plot=plot))
        
        if 'temporada' not in item.title and item.title not in scrapedurl and scrapedtipo =='Capitulo' and item.temp =='':
            if item.temp == '': temp = '1'
            title = item.contentSerieName+' '+temp+'x'+scrapedtitle+' ('+idioma+')'
            if '#' not in scrapedurl:
               itemlist.append( Item(channel=item.channel, action="findvideos" , title=title, fulltitle=item.fulltitle, url=url, thumbnail=item.thumbnail, plot=plot))
        
        if 'temporada' not in item.title and item.title not in scrapedurl and scrapedtipo =='Pelicula':
            title = scrapedtipo +' '+scrapedtitle
            itemlist.append( Item(channel=item.channel, action="findvideos" , title=title, fulltitle=item.fulltitle, url=url, thumbnail=item.thumbnail, plot=plot))




        #elif 'temporada' not in item.title and item.title not in scrapedurl and scrapedtipo !='Capitulo':
        #    title = scrapedtipo +' '+scrapedtitle
        #    itemlist.append( Item(channel=item.channel, action="findvideos" , title=title, fulltitle=item.fulltitle, url=url, thumbnail=item.thumbnail, plot=plot))
    #if config.get_library_support() and len(itemlist) > 0:
    #    itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta serie a la biblioteca[/COLOR]', url=item.url,
    #                            action="add_serie_to_library", extra="episodios", contentSerieName=item.contentSerieName, extra1 = item.extra1))
    return itemlist            
                                 
    


    
