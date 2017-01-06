# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para yaske
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import re
import sys
import urllib
import urlparse

from core import config
from core import logger
from core import scrapertools
from core import servertools
from core.item import Item


DEBUG = config.get_setting("debug")
CHANNEL_HOST = 'http://www.yaske.ro/'
HEADER = [
    ['User-Agent', 'Mozilla/5.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Referer', CHANNEL_HOST],
    ['Connection', 'keep-alive']
]


def mainlist(item):
    logger.info("pelisalacarta.yaske mainlist")

    itemlist = []
    itemlist.append( Item(channel=item.channel, title="Novedades"          , action="peliculas",       url="http://www.yaske.ro/"))
    itemlist.append( Item(channel=item.channel, title="Por año"            , action="menu_buscar_contenido",      url="http://www.yaske.ro/", extra="year"))
    itemlist.append( Item(channel=item.channel, title="Por género"         , action="menu_buscar_contenido", url="http://www.yaske.ro/", extra="gender"))
    itemlist.append( Item(channel=item.channel, title="Por calidad"        , action="menu_buscar_contenido",  url="http://www.yaske.ro/", extra="quality"))
    itemlist.append( Item(channel=item.channel, title="Por idioma"         , action="menu_buscar_contenido",    url="http://www.yaske.ro/", extra="language"))
    itemlist.append( Item(channel=item.channel, title="Buscar"             , action="search") )

    return itemlist

def search(item,texto):

    logger.info("pelisalacarta.yaske search")
    itemlist = []

    try:
        item.url = "http://www.yaske.ro/search/%s"
        item.url = item.url % texto
        item.extra = ""
        itemlist.extend(peliculas(item))
        itemlist = sorted(itemlist, key=lambda Item: Item.title) 

        return itemlist

    except:
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line )
        return []


def newest(categoria):
    itemlist = []
    item = Item()
    try:
        if categoria == 'peliculas':
            item.url = "http://www.yaske.ro/"
        elif categoria == 'infantiles':
            item.url = "http://www.yaske.ro/custom/?gender=animation"
        else:
            return []

        itemlist = peliculas(item)
        if itemlist[-1].title == ">> Página siguiente":
            itemlist.pop()

    # Se captura la excepción, para no interrumpir al canal novedades si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []

    return itemlist

def peliculas(item):
    logger.info("pelisalacarta.yaske peliculas")
	

    data = scrapertools.anti_cloudflare(item.url,headers=HEADER, host=CHANNEL_HOST)
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)

    # Extrae las entradas
    '''
       <li class="item-movies c8">
        <div class="tooltipyk">
        <a class="image-block" href="http://www.yaske.ro/es/pelicula/0010962/ver-the-walking-dead-7x02-online.html" title="The Walking Dead 7x02">
        <img src="http://www.yaske.ro/upload/images/b59808b9b505c15283159099ff7320c6.jpg" alt="The Walking Dead 7x02" width="140" height="200" />
        </a>
    <span class="tooltipm">
        <img class="callout" src="http://www.yaske.ro/upload/tooltip/callout_black.gif" />
        <div class="moTitulo"><b>Título: </b>The Walking Dead 7x02<br><br></div>
        <div class="moSinopsis"><b>Sinopsis: </b>Array<br><br></div>
        <div class="moYear"><b>Año: </b>2016</div>
        </span>
       </div>
        <ul class="bottombox">
            <li><a href="http://www.yaske.ro/es/pelicula/0010962/ver-the-walking-dead-7x02-online.html" title="The Walking Dead 7x02">
                The Walking Dead 7x02    	</a></li>
            <li>Accion, Thrillers, Terror</li>
            <li><img src='http://www.yaske.ro/theme/01/data/images/flags/en_es.png' title='English SUB Spanish' width='25'/> <img src='http://www.yaske.ro/theme/01/data/images/flags/la_la.png' title='Latino ' width='25'/> <img src='http://www.yaske.ro/theme/01/data/images/flags/es_es.png' title='Spanish ' width='25'/> </li>
            <li>        	<img class="opa3" src="http://storage.ysk.pe/b6b5870914222d773c5b76234978e376.png" height="22" border="0">
            </li>
        </ul>
        <div class="quality">Hd Real 720</div>
        <div class="view"><span>view: 6895</span></div>
    </li>
    '''
    patron  = '<li class="item-movies.*?'
    patron += '<a class="image-block" href="([^"]+)" title="([^"]+)">'
    patron += '<img src="([^"]+).*?'
    patron += '<ul class="bottombox">.*?<li>(<img.*?)</li>.*?</ul>'
    patron += '<div class="quality">([^<]+)</div>'
 
    matches = re.compile(patron,re.DOTALL).findall(data)
    #logger.debug(matches)
    itemlist = []

    for scrapedurl, scrapedtitle, scrapedthumbnail, idiomas, calidad in matches:

        patronidiomas = "<img src='[^']+' title='([^']+)'"
        matchesidiomas = re.compile(patronidiomas,re.DOTALL).findall(idiomas)

        idiomas_disponibles = ""
        for idioma in matchesidiomas:
            idiomas_disponibles = idiomas_disponibles + idioma.strip() + "/"

        if len(idiomas_disponibles)>0:
            idiomas_disponibles = "["+idiomas_disponibles[:-1]+"]"
        
        title = scrapedtitle.strip()+" "+idiomas_disponibles+"["+calidad+"]"
        title = scrapertools.htmlclean(title)

        contentTitle = scrapertools.htmlclean(scrapedtitle.strip())

        url = scrapedurl

        thumbnail = scrapedthumbnail
        scrapedplot = ""

        itemlist.append( Item(channel=item.channel, action="findvideos", title=title , url=url , thumbnail=thumbnail , plot=scrapedplot , fulltitle=scrapertools.htmlclean(scrapedtitle.strip()), viewmode="movie", folder=True, hasContentDetails="true", contentTitle=contentTitle, contentThumbnail=thumbnail) )

    # Extrae el paginador
    patronvideos  = "<a href='([^']+)'>\&raquo\;</a>"
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=item.channel, action="peliculas", title=">> Página siguiente" , url=scrapedurl , folder=True) )

    return itemlist

def menu_buscar_contenido(item):
    logger.info("pelisalacarta.yaske menu_categorias")

    data = scrapertools.anti_cloudflare(item.url,headers=HEADER, host=CHANNEL_HOST)
    #logger.info("data="+data)

    data = scrapertools.get_match(data,'<select name="'+item.extra+'"(.*?)</select>')
    #logger.info("data="+data)

    # Extrae las entradas
    patron  = "<option value='([^']+)'>([^<]+)</option>"
    matches = re.compile(patron,re.DOTALL).findall(data)

    itemlist = []

    for scrapedurl,scrapedtitle in matches:
        scrapedthumbnail = ""
        scrapedplot = ""
        
        
        if item.extra == 'gender':
            url = "http://www.yaske.ro/genero/"+scrapedurl
        else:
            url = "http://www.yaske.ro/custom/?"+item.extra+"="+scrapedurl

        itemlist.append( Item(channel=item.channel, action="peliculas", title=scrapedtitle , url=url , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )

    return sorted(itemlist, key=lambda i:  i.title.lower())

def findvideos(item):
    logger.info("pelisalacarta.yaske findvideos url="+item.url)

    # Descarga la página
    data = scrapertools.anti_cloudflare(item.url,headers=HEADER, host=CHANNEL_HOST)

    item.plot = scrapertools.find_single_match(data,'<meta name="sinopsis" content="([^"]+)"')
    item.plot = scrapertools.htmlclean(item.plot)
    item.contentPlot = item.plot

    # Extrae las entradas
    '''
    <tr bgcolor="">
    <td height="32" align="center"><a class="btn btn-mini enlace_link" style="text-decoration:none;" rel="nofollow" target="_blank" title="Ver..." href="http://www.yaske.net/es/reproductor/pelicula/2141/44446/"><i class="icon-play"></i><b>&nbsp; Opcion &nbsp; 04</b></a></td>
    <td align="left"><img src="http://www.google.com/s2/favicons?domain=played.to"/>played</td>
    <td align="center"><img src="http://www.yaske.net/theme/01/data/images/flags/la_la.png" width="21">Lat.</td>
    <td align="center" class="center"><span title="" style="text-transform:capitalize;">hd real 720</span></td>
    <td align="center"><div class="star_rating" title="HD REAL 720 ( 5 de 5 )">
    <ul class="star"><li class="curr" style="width: 100%;"></li></ul>
    </div>
    </td> <td align="center" class="center">2553</td> </tr>
    '''

    patron  = '<tr bgcolor=(.*?)</tr>'
    matches = re.compile(patron,re.DOTALL).findall(data)

    itemlist = []

    #n = 1
    for tr in matches:
        logger.info("tr="+tr)
        try:
            title = scrapertools.get_match(tr,'<b>([^<]+)</b>')
            server = scrapertools.get_match(tr,'"http\://www.google.com/s2/favicons\?domain\=([^"]+)"')

            # <td align="center"><img src="http://www.yaske.net/theme/01/data/images/flags/la_la.png" width="19">Lat.</td>
            idioma = scrapertools.get_match(tr,'<img src="http://www.yaske.[a-z]+/theme/01/data/images/flags/([a-z_]+).png"[^>]+>[^<]*<')
            subtitulos = scrapertools.get_match(tr,'<img src="http://www.yaske.[a-z]+/theme/01/data/images/flags/[^"]+"[^>]+>([^<]*)<')
            calidad = scrapertools.get_match(tr,'<td align="center" class="center"[^<]+<span title="[^"]*" style="text-transform.capitalize.">([^<]+)</span></td>')
            
            #<a [....] href="http://api.ysk.pe/noref/?u=< URL Vídeo >">
            url = scrapertools.get_match(tr,'<a.*?href="([^"]+)"')

            # Para extraer netutv se necesita en la actualidad pasar por varias páginas con lo que relentiza mucho la carga.
            # De momento mostrará "No hay nada que reproducir"
            '''
            if "/netu/tv/" in url:
                import base64
                ###################################################
                # Añadido 17-09-14
                ###################################################
                try: data = scrapertools.cache_page(url,headers=getSetCookie(url1))
                except: data = scrapertools.cache_page(url)
                ###################################################
                match_b64_1 = 'base64,([^"]+)"'
                b64_1 = scrapertools.get_match(data, match_b64_1)
                utf8_1 = base64.decodestring(b64_1)
                match_b64_inv = "='([^']+)';"
                b64_inv = scrapertools.get_match(utf8_1, match_b64_inv)
                b64_2 = b64_inv[::-1]
                utf8_2 = base64.decodestring(b64_2).replace("%","\\").decode('unicode-escape')
                id_video = scrapertools.get_match(utf8_2,'<input name="vid" id="text" value="([^"]+)">')
                url = "http://netu.tv/watch_video.php?v="+id_video
            '''

            title = title.replace("&nbsp;","")

            if "es_es" in idioma:
                scrapedtitle = title + " en "+server.strip()+" [ESP]["+calidad+"]"
            elif "la_la" in idioma:
                scrapedtitle = title + " en "+server.strip()+" [LAT]["+calidad+"]"
            elif "en_es" in idioma:
                scrapedtitle = title + " en "+server.strip()+" [SUB]["+calidad+"]"
            elif "en_en" in idioma:
                scrapedtitle = title + " en "+server.strip()+" [ENG]["+calidad+"]"
            else:
                scrapedtitle = title + " en "+server.strip()+" ["+idioma+" / "+subtitulos+"]["+calidad+"]"
            scrapedtitle = scrapertools.entityunescape(scrapedtitle)
            scrapedtitle = scrapedtitle.strip()

            scrapedurl = url

            scrapedthumbnail = servertools.guess_server_thumbnail(scrapedtitle)

            logger.info("server="+server+", scrapedurl="+scrapedurl)
            if scrapedurl.startswith("http") and not "olimpo.link" in scrapedurl:
                itemlist.append( Item(channel=item.channel, action="play", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , folder=False, parentContent=item) )
        except:
            import traceback
            logger.info("Excepcion: "+traceback.format_exc())

    return itemlist

def play(item):
    logger.info("pelisalacarta.yaske play item.url="+item.url)
    
    itemlist=[]

    # http%3A%2F%2Folo.gg%2Fs%2FcJinsNv1%3Fs%3Dhttp%253A%252F%252Fwww.nowvideo.to%252Fvideo%252F9c8bf2ed9d4fd
    data = urllib.unquote(item.url)

    logger.info("pelisalacarta.yaske play item.url="+data)

    # http://olo.gg/s/cJinsNv1?s=http%3A%2F%2Fwww.nowvideo.to%2Fvideo%2F9c8bf2ed9d4fd
    newdata = scrapertools.find_single_match(data,'olo.gg/s/[a-zA-Z0-9]+.s.(.*?)$')
    if newdata!="":
        data = newdata
    logger.info("pelisalacarta.yaske play item.url="+data)

    data = urllib.unquote(data)
    logger.info("pelisalacarta.yaske play item.url="+data)

    itemlist = servertools.find_video_items(item=item,data=data)
    for newitem in itemlist:
        newitem.fulltitle = item.fulltitle
    
    return itemlist
