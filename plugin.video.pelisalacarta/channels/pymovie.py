# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canal (pymovie) por Hernan_Ar_c
# ------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from core import servertools


DEBUG = config.get_setting("debug")
host ="http://www.pymovie.com.mx"

headers = [['User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'],
          ['Referer', host]]


tgenero = {"comedia":"https://s32.postimg.org/q7g2qs90l/comedia.png",
           "drama":"https://s32.postimg.org/e6z83sqzp/drama.png",
           "accion":"https://s32.postimg.org/4hp7gwh9x/accion.png",
           "aventura":"https://s32.postimg.org/whwh56is5/aventura.png",
           "romance":"https://s31.postimg.org/y7vai8dln/romance.png",
           "animacion":"https://s32.postimg.org/rbo1kypj9/animacion.png",
           "ciencia ficcion":"https://s32.postimg.org/6hp3tsxsl/ciencia_ficcion.png",
           "terror":"https://s32.postimg.org/ca25xg0ed/terror.png",
           "musical":"https://s31.postimg.org/7i32lca7f/musical.png",
           "deporte":"https://s31.postimg.org/pdc8etc0r/deporte.png",
           "artes Marciales":"https://s32.postimg.org/5e80taodh/artes_marciales.png",
           "intriga":"https://s32.postimg.org/xc2ovcqfp/intriga.png",
           "infantil":"https://s32.postimg.org/i53zwwgsl/infantil.png",
           "mexicanas":"https://s30.postimg.org/rplllq9wx/mexicana.png",
           "espionaje":"https://s30.postimg.org/myjqzg6xt/espionaje.png",
           "biografia":"https://s23.postimg.org/u49p87o3f/biografia.png"}


tcalidad = {'hd-1080':'[COLOR limegreen]HD-1080[/COLOR]','hd-720':'[COLOR limegreen]HD-720[/COLOR]','blueray':'[COLOR limegreen]BLUERAY[/COLOR]','dvd':'[COLOR limegreen]DVD[/COLOR]','cam':'[COLOR red]CAM[/COLOR]'}

tcalidad2 = {'hd-1080':'https://s24.postimg.org/vto15vajp/hd1080.png','hd-720':'https://s28.postimg.org/wllbt2kgd/hd720.png','blueray':'','dvd':'https://s31.postimg.org/6sksfqarf/dvd.png','cam':'https://s29.postimg.org/c7em44e9j/cam.png'}


def mainlist(item):
    logger.info("pelisalacarta.channels.pymovie mainlist")

    itemlist = []
    
    itemlist.append( item.clone(title="Peliculas", action="menupeliculas",thumbnail='https://s31.postimg.org/4g4lytrqj/peliculas.png', fanart='https://s31.postimg.org/4g4lytrqj/peliculas.png', extra='peliculas/'))
    
    itemlist.append( itemlist[-1].clone(title="Series", action="menuseries",thumbnail='https://s32.postimg.org/544rx8n51/series.png', fanart='https://s32.postimg.org/544rx8n51/series.png', extra='peliculas/'))
    
    
    itemlist.append( itemlist[-1].clone (title="Documentales", action="menudocumental",thumbnail='https://s21.postimg.org/i9clk3u6v/documental.png', fanart='https://s21.postimg.org/i9clk3u6v/documental.png', extra='documental'))

    #itemlist.append( Item(channel=item.channel, title="Documentales", action="lista", url=host+'documentales/pag-1', thumbnail='https://s21.postimg.org/i9clk3u6v/documental.png', fanart='https://s21.postimg.org/i9clk3u6v/documental.png', extra='documentales/'))
    
    return itemlist

def menupeliculas(item):

    logger.info("pelisalacarta.channels.pymovie menupeliculas")
    itemlist = []
    
    itemlist.append( Item(channel=item.channel, title="Ultimas", action="lista", url=host+'/Ordenar/Estreno/?page=1', thumbnail='https://s31.postimg.org/3ua9kwg23/ultimas.png', fanart='https://s31.postimg.org/3ua9kwg23/ultimas.png', extra='Estreno'))

    itemlist.append( Item(channel=item.channel, title="Todas", action="lista", url=host+'?page=1', thumbnail='https://s12.postimg.org/iygbg8ip9/todas.png', fanart='https://s12.postimg.org/iygbg8ip9/todas.png', extra='todas'))
    
    itemlist.append( Item(channel=item.channel, title="Generos", action="seccion", url=host, thumbnail='https://s31.postimg.org/szbr0gmkb/generos.png', fanart='https://s31.postimg.org/szbr0gmkb/generos.png', extra='generos'))

    itemlist.append( Item(channel=item.channel, title="Alfabetico", action="lista", url=host+'/Ordenar/Alfabetico/?page=1', thumbnail='https://s31.postimg.org/c3bm9cnl7/a_z.png', fanart='https://s31.postimg.org/c3bm9cnl7/a_z.png', extra='Alfabetico'))

    itemlist.append( Item(channel=item.channel, title="Calidad", action="seccion", url=host, thumbnail='https://s23.postimg.org/ui42030wb/calidad.png', fanart='https://s23.postimg.org/ui42030wb/calidad.png', extra='calidad'))

    itemlist.append( Item(channel=item.channel, title="Mas Vistas", action="lista", url=host+'/Ordenar/MasVistas/?page=1', thumbnail='https://s32.postimg.org/466gt3ipx/vistas.png', fanart='https://s32.postimg.org/466gt3ipx/vistas.png', extra='Estreno'))

    itemlist.append( Item(channel=item.channel, title="Mas Votadas", action="lista", url=host+'/Ordenar/MasVotos/?page=1', thumbnail='https://s31.postimg.org/9ooh78xej/votadas.png', fanart='https://s31.postimg.org/9ooh78xej/votadas.png', extra='Estreno'))

    itemlist.append( Item(channel=item.channel, title="Calificacion", action="lista", url=host+'/Ordenar/Calificacion/?page=1', thumbnail='https://s28.postimg.org/r1xdh0xz1/calificacion.png', fanart='https://s28.postimg.org/r1xdh0xz1/calificacion.png', extra='Estreno'))
    
    return itemlist


def menuseries(item):

    logger.info("pelisalacarta.channels.pymovie menuseries")
    itemlist = []
    
    itemlist.append( Item(channel=item.channel, title="Ultimas", action="lista", url=host+"/Series-estreno/?page=1",thumbnail='https://s31.postimg.org/3ua9kwg23/ultimas.png', fanart='https://s31.postimg.org/3ua9kwg23/ultimas.png', extra='series'))
        
    itemlist.append( Item(channel=item.channel, title="Generos", action="seccion", url=host, thumbnail='https://s31.postimg.org/szbr0gmkb/generos.png', fanart='https://s31.postimg.org/szbr0gmkb/generos.png', extra='series-generos'))

    itemlist.append( Item(channel=item.channel, title="Alfabetico", action="lista", url=host+'/Ordernar-Serie/Alfabetico/?page=1', thumbnail='https://s31.postimg.org/c3bm9cnl7/a_z.png', fanart='https://s31.postimg.org/c3bm9cnl7/a_z.png', extra='series-alpha'))

   
    itemlist.append( Item(channel=item.channel, title="Mas Vistas", action="lista", url=host+'/Ordernar-Serie/MasVistas/?page=1', thumbnail='https://s32.postimg.org/466gt3ipx/vistas.png', fanart='https://s32.postimg.org/466gt3ipx/vistas.png', extra='series-masvistas'))

    itemlist.append( Item(channel=item.channel, title="Mas Votadas", action="lista", url=host+'/Ordernar-Serie/Masvotos/?page=1', thumbnail='https://s31.postimg.org/9ooh78xej/votadas.png', fanart='https://s31.postimg.org/9ooh78xej/votadas.png', extra='series-masvotadas'))

    itemlist.append( Item(channel=item.channel, title="Recomendadas", action="lista", url=host+'/Ordernar-Serie/Recomendadas/?page=1', thumbnail='https://s31.postimg.org/4bsjyc4iz/recomendadas.png', fanart='https://s31.postimg.org/4bsjyc4iz/recomendadas.png', extra='series-recomendadas'))
    
        
    return itemlist

def menudocumental(item):
	logger.info("pelisalacarta.channels.pymovie menudocumental")
	itemlist =[]

	itemlist.append( Item(channel=item.channel, title="Todas", action="lista", url=host+"/Documentales/?page=1",thumbnail='https://s12.postimg.org/iygbg8ip9/todas.png', fanart='https://s12.postimg.org/iygbg8ip9/todas.png', extra='documental'))

	itemlist.append( Item(channel=item.channel, title="Alfabetico", action="lista", url=host+"/OrdenarDocumental/Alfabetico/?page=1",thumbnail='https://s31.postimg.org/c3bm9cnl7/a_z.png', fanart='https://s31.postimg.org/c3bm9cnl7/a_z.png', extra='documental'))

	itemlist.append( Item(channel=item.channel, title="Mas Vistas", action="lista", url=host+"/OrdenarDocumental/MasVistas/?page=1",thumbnail='https://s32.postimg.org/466gt3ipx/vistas.png', fanart='https://s32.postimg.org/466gt3ipx/vistas.png', extra='documental'))

	

	return itemlist


def lista(item):
    logger.info("pelisalacarta.channels.pymovie lista")
    
    
    if item.extra =='series':
	    accion = 'episodios'
    elif 'series-'in item.extra:
	    accion = 'temporadas'
    else:
	    accion = 'findvideos'

    itemlist = []
    data = scrapertools.cache_page(item.url)
    
    if 'series' in item.extra or item.extra == 'documental':
       patron = '<h2 itemprop="name" >([^<]+)<\/h2><a href="([^.]+)" title=".*?" ><img.*?src="([^"]+)".*?class=".*?boren2"\/([^<]+)'
    else:
       patron = '<h2 itemprop="name" >([^<]+)<\/h2><a href="([^.]+)" title=".*?" ><img.*?src="([^"]+)".*?class=".*?boren2".*?>([^<]+)'
    matches = re.compile(patron,re.DOTALL).findall(data)

    for scrapedtitle, scrapedurl, scrapedthumbnail, scrapedcalidad in matches:
        url = scrapertools.decodeHtmlentities(host+scrapedurl)
        
        scrapedcalidad = scrapedcalidad.strip(' ')
        scrapedcalidad = scrapedcalidad.strip('p')
        scrapedcalidad = scrapedcalidad.lower()
        if 'series' in item.extra or item.extra == 'documental':
           title = scrapertools.decodeHtmlentities(scrapedtitle)
        else:
           calidad = tcalidad[scrapedcalidad] 
           title = scrapertools.decodeHtmlentities(scrapedtitle)+' ('+calidad+') '
        
        
        thumbnail = scrapedthumbnail
        fanart =''
        plot=''
        
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action=accion , title=title , url=url, thumbnail=thumbnail, plot=plot, fanart=fanart, contentSerieName = scrapedtitle, contentTitle = scrapedtitle, extra = item.extra))
       
# #Paginacion

    if itemlist !=[]:
        actual_page_url = item.url
        next_page = scrapertools.find_single_match(data,'<a href="\?page=([^"]+)" class="next">next &')
        while item.url[-1] != '=':
        	item.url=item.url[:-1]
        next_page_url= item.url+next_page
        import inspect
        if next_page !='':
           itemlist.append(Item(channel = item.channel, action = "lista", title = 'Siguiente >>>', url = next_page_url, thumbnail='https://s32.postimg.org/4zppxf5j9/siguiente.png',extra=item.extra))
    return itemlist
    

def temporadas(item):
    logger.info("pelisalacarta.channels.pymovie temporadas")
    itemlist = []
    templist = []
    data = scrapertools.cache_page(item.url)
    
    patron = 'class="listatemporadas" ><a href="([^"]+)" title=".*?"  ><img src="([^"]+)"  width="80" height="100" title=".*?alt=".*?<h3>([^<]+)<'
    matches = re.compile(patron,re.DOTALL).findall(data)
    
    for scrapedurl, scrapedthumbnail, scrapedtitle in matches:
        url = host+scrapedurl
        title = scrapedtitle
        thumbnail = scrapedthumbnail
        plot = ''
        fanart = ''
        contentSeasonNumber = scrapedtitle.replace('Temporada ','')
        
        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        itemlist.append( Item(channel=item.channel, action="episodios" , title=title , fulltitle=item.title, url=url, thumbnail=thumbnail, plot=plot, fanart = fanart, contentSerieName = item.contentSerieName, contentSeasonNumber = contentSeasonNumber))

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

    logger.info("pelisalacarta.channels.pymovie episodios")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    patron = '<a href="\/VerCapitulo\/([^"]+)">'
    matches = re.compile(patron,re.DOTALL).findall(data)
    
    if item.contentSeasonNumber == '':
       temp = 0
    else:
       temp = 1
    
    if temp == 0:
       	  contentSeasonNumber = re.findall(r'\d',item.title)
       	  item.contentSeasonNumber = contentSeasonNumber[0]

    ep = 1
    for scrapedtitle in matches:
       
       scrapedtitle = scrapedtitle.replace (item.contentSeasonNumber+'x'+'0'+str(ep),'')
       url = host+'/VerCapitulo/'+scrapedtitle.replace(' ','-')
       title = item.contentSeasonNumber+'x'+str(ep)+' '+scrapedtitle.strip('/')
       
       thumbnail = item.thumbnail
       plot = ''
       fanart = ''
       plot = ''
       contentEpisodeNumber = str(ep)
              
       itemlist.append( Item(channel=item.channel, action="findvideos" , title=title , fulltitle=item.title, url=url, thumbnail=thumbnail, plot=plot, fanart = fanart, extra='series', contentSerieName = item.contentSerieName, contentSeasonNumber = item.contentSeasonNumber, contentEpisodeNumber = contentEpisodeNumber))
       ep = ep+1
   
    return itemlist       


def seccion(item):
    
    logger.info("pelisalacarta.channels.pymovie generos")
    itemlist = []
    data = scrapertools.cache_page(item.url)
    patron = '<option class="opselect" value="([^"]+)".*?>([^<]+)<\/option>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if item.extra == 'generos':
    	oplista = tgenero
    	opdir = '/Categoria/'
    elif item.extra == 'calidad':
        oplista = tcalidad
    	opdir = '/Calidad/'
    elif item.extra == 'series-generos':
    	oplista = tgenero
    	opdir = '/Categoria-Series/'
        

    for scrapeddir, scrapedtitle in matches:
    
        url = item.url+opdir+scrapeddir+'/?page=1'
        title = scrapedtitle.upper()
      
        if 'generos' in item.extra and scrapedtitle.lower() in oplista:
           thumbnail =oplista[scrapedtitle.lower()]
           fanart= oplista[scrapedtitle.lower()]

        elif 'calidad' in item.extra and scrapedtitle.lower() in oplista:
           thumbnail =tcalidad2[scrapedtitle.lower()]
           fanart= tcalidad[scrapedtitle.lower()]

        else:
           thumbnail =''
           fanart= ''

        if (DEBUG): logger.info("title=["+title+"], url=["+url+"], thumbnail=["+thumbnail+"])")
        if scrapedtitle.lower() in oplista:
           itemlist.append( Item(channel=item.channel, action="lista" , title=title , fulltitle=item.title, url=url, thumbnail=thumbnail, fanart = fanart, extra = item.extra))
    return itemlist
    

def findvideos(item):
	logger.info("pelisalacarta.channels.pymovie findvideos")
	itemlist =[]
	audio = {'Latino':'[COLOR limegreen]LATINO[/COLOR]','Español':'[COLOR yellow]ESPAÑOL[/COLOR]','Ingles':'[COLOR red]ORIGINAL SUBTITULADO[/COLOR]', 'Latino-Ingles':'DUAL'}
	data = scrapertools.cache_page(item.url)
			
	if item.extra != 'series':
	   patron ='data-video="([^"]+)" class="reproductorVideo"><ul><li>([^<]+)<\/li><li>([^<]+)<\/li>'
	   tipotitle = item.contentTitle
	elif item.extra == 'series':
	   tipotitle = item.contentSeasonNumber+'x'+item.contentEpisodeNumber+' '+item.contentSerieName
	   patron = '<li class="enlaces-l"><a href="([^"]+)" target="_blank"><ul><li>([^<]+)<.*?>([^<]+)<.*?>Reproducir<'
	
	matches = re.compile(patron,re.DOTALL).findall(data)

	if item.extra != 'documental':
		n=0
		
		for scrapedurl, scrapedcalidad, scrapedaudio in matches:
		   if 'series' in item.extra:  
		      datab = scrapertools.cache_page(host+scrapedurl)
		      url = scrapertools.find_single_match(datab,'class="reproductor"><iframe src="([^"]+)"')
		      print url+'esta es la direccion'
		   else:
		      url = scrapedurl
		   
		   title = tipotitle
		   idioma = audio[scrapedaudio]
		   itemlist.extend(servertools.find_video_items(data=url))
		   if n < len(itemlist):
		      itemlist[n].title = tipotitle+ ' ('+idioma+' ) '+'('+itemlist[n].server+' )'
		   n = n+1
	else:
		url = scrapertools.find_single_match(data,'class="reproductor"><iframe src="([^"]+)"')
		itemlist.extend(servertools.find_video_items(data=url))




	for videoitem in itemlist:
	   if item.extra == 'documental':
	   	  videoitem.title = item.title+' ('+videoitem.server+')'
	   videoitem.channel=item.channel
	   videoitem.action="play"
	   videoitem.folder=False


	if config.get_library_support() and len(itemlist) > 0 and item.extra !='findvideos':
          itemlist.append(Item(channel=item.channel, title='[COLOR yellow]Añadir esta pelicula a la biblioteca[/COLOR]', url=item.url,
                             action="add_pelicula_to_library", extra="findvideos", contentTitle = item.contentTitle))
	
	return itemlist




 




