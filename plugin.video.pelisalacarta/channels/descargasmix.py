# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para Descargasmix
# Por SeiTaN, robalo y Cmos
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import re
import urllib

from core import config
from core import logger
from core import scrapertools
from core import servertools
from core.item import Item


__modo_grafico__ = config.get_setting("modo_grafico", "descargasmix")
__perfil__ = int(config.get_setting("perfil", "descargasmix"))

# Fijar perfil de color            
perfil = [['0xFFFFE6CC', '0xFFFFCE9C', '0xFF994D00'],
          ['0xFFA5F6AF', '0xFF5FDA6D', '0xFF11811E'],
          ['0xFF58D3F7', '0xFF2E9AFE', '0xFF2E64FE']]
color1, color2, color3 = perfil[__perfil__]

DEBUG = config.get_setting("debug")
DEFAULT_HEADERS = [["User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"]]


def mainlist(item):
    logger.info("pelisalacarta.channels.descargasmix mainlist")
    itemlist = []
    item.text_color = color1
    
    itemlist.append(item.clone(title="Películas", action="lista", fanart="http://i.imgur.com/c3HS8kj.png"))
    itemlist.append(item.clone(title="Series", action="lista_series", fanart="http://i.imgur.com/9loVksV.png"))
    itemlist.append(item.clone(title="Documentales", action="entradas", url="http://desmix.net/documentales/",
                               fanart="http://i.imgur.com/Q7fsFI6.png"))
    itemlist.append(item.clone(title="Anime", action="entradas", url="http://desmix.net/anime/",
                               fanart="http://i.imgur.com/whhzo8f.png"))
    itemlist.append(item.clone(title="Deportes", action="entradas", url="http://desmix.net/deportes/",
                               fanart="http://i.imgur.com/ggFFR8o.png"))
    itemlist.append(item.clone(title="", action=""))
    itemlist.append(item.clone(title="Buscar...", action="search"))
    itemlist.append(item.clone(action="configuracion", title="Configurar canal...", text_color="gold", folder=False))

    return itemlist


def configuracion(item):
    from platformcode import platformtools
    platformtools.show_channel_settings()
    if config.is_xbmc():
        import xbmc
        xbmc.executebuiltin("Container.Refresh")


def search(item, texto):
    logger.info("pelisalacarta.channels.descargasmix search")
    try:
        item.url= "http://desmix.net/?s=" + texto
        return busqueda(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []


def busqueda(item):
    logger.info("pelisalacarta.channels.descargasmix busqueda")
    itemlist = []
    data = scrapertools.downloadpage(item.url)

    contenido = ['Películas', 'Series', 'Documentales', 'Anime', 'Deportes', 'Miniseries', 'Vídeos']
    bloque = scrapertools.find_single_match(data, '<div id="content" role="main">(.*?)<div id="sidebar" '
                                                  'role="complementary">')
    patron = '<a class="clip-link".*?href="([^"]+)".*?<img alt="([^"]+)" src="([^"]+)"' \
             '.*?<p class="stats">(.*?)</p>'
    matches = scrapertools.find_multiple_matches(bloque, patron)
    for scrapedurl, scrapedtitle, scrapedthumbnail, scrapedcat in matches:
        if not [True for c in contenido if c in scrapedcat]:
            continue
        if not scrapedthumbnail.startswith("http"):
                scrapedthumbnail = "http:"+scrapedthumbnail
        scrapedthumbnail = scrapedthumbnail.replace("-129x180", "")
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        if ("Películas" in scrapedcat or "Documentales" in scrapedcat) and not "Series" in scrapedcat:
            titulo = scrapedtitle.split("[")[0]
            itemlist.append(item.clone(action="findvideos", title=scrapedtitle, url=scrapedurl,
                                       thumbnail=scrapedthumbnail, fulltitle=titulo, context=["buscar_trailer"], contentTitle=titulo, contentType="movie"))
        else:
            itemlist.append(item.clone(action="episodios", title=scrapedtitle, url=scrapedurl,  context=["buscar_trailer"],
                                       thumbnail=scrapedthumbnail, fulltitle=scrapedtitle, contentTitle=scrapedtitle,
                                       show=scrapedtitle, contentType="tvshow"))

    next_page = scrapertools.find_single_match(data, '<a class="nextpostslink".*?href="([^"]+)"')
    if next_page != "":
        itemlist.append(item.clone(action="busqueda", title=">> Siguiente", url=next_page))

    return itemlist


def lista(item):
    logger.info("pelisalacarta.channels.descargasmix lista")
    itemlist = []

    itemlist.append(item.clone(title="Novedades", action="entradas", url="http://desmix.net/peliculas"))
    itemlist.append(item.clone(title="Estrenos", action="entradas", url="http://desmix.net/peliculas/estrenos"))
    itemlist.append(item.clone(title="Dvdrip", action="entradas", url="http://desmix.net/peliculas/dvdrip"))
    itemlist.append(item.clone(title="HD (720p/1080p)", action="entradas", url="http://desmix.net/peliculas/hd"))
    itemlist.append(item.clone(title="HDRIP", action="entradas", url="http://desmix.net/peliculas/hdrip"))
    itemlist.append(item.clone(title="Latino", action="entradas",
                               url="http://desmix.net/peliculas/latino-peliculas"))
    itemlist.append(item.clone(title="VOSE", action="entradas", url="http://desmix.net/peliculas/subtituladas"))
    itemlist.append(item.clone(title="3D", action="entradas", url="http://desmix.net/peliculas/3d"))
    itemlist.append(item.clone(title="Géneros", action="generos", url="http://desmix.net/peliculas/"))

    return itemlist


def lista_series(item):
    logger.info("pelisalacarta.channels.descargasmix lista_series")
    itemlist = []

    itemlist.append(item.clone(title="Novedades", action="entradas", url="http://desmix.net/series/"))
    itemlist.append(item.clone(title="Miniseries", action="entradas", url="http://desmix.net/series/miniseries"))
    itemlist.append(item.clone(title="Géneros", action="generos", url="http://desmix.net/series/"))

    return itemlist


def entradas(item):
    logger.info("pelisalacarta.channels.descargasmix entradas")
    itemlist = []
    item.text_color = color2
    data = scrapertools.downloadpage(item.url)

    bloque = scrapertools.find_single_match(data, '<div id="content" role="main">(.*?)<div id="sidebar" '
                                                  'role="complementary">')
    contenido = ["series", "deportes", "anime", 'miniseries']
    c_match = [True for match in contenido if match in item.url]
    #Patron dependiendo del contenido
    if True in c_match:
        patron = '<a class="clip-link".*?href="([^"]+)".*?<img alt="([^"]+)" src="([^"]+)"' \
                 '.*?<span class="overlay(|[^"]+)">'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedurl, scrapedtitle, scrapedthumbnail, scrapedinfo in matches:
            if scrapedinfo != "":
                scrapedinfo = "  [" + scrapedinfo.replace(" ", "").replace("-", " ").capitalize() + "]"
            titulo = scrapedtitle+scrapedinfo	
            titulo = scrapertools.decodeHtmlentities(titulo)
            scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
            if not scrapedthumbnail.startswith("http"):
                scrapedthumbnail = "http:"+scrapedthumbnail
            scrapedthumbnail = scrapedthumbnail.replace("-129x180", "")
            scrapedthumbnail = scrapedthumbnail.rsplit("/", 1)[0]+"/"+urllib.quote(scrapedthumbnail.rsplit("/", 1)[1])
            if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
            if "series" in item.url or "anime" in item.url:
                item.show = scrapedtitle
            itemlist.append(item.clone(action="episodios", title=titulo, url=scrapedurl, thumbnail=scrapedthumbnail,
                                       fulltitle=scrapedtitle, context=["buscar_trailer"], contentTitle=scrapedtitle, contentType="tvshow"))
    else:
        patron = '<a class="clip-link".*?href="([^"]+)".*?<img alt="([^"]+)" src="([^"]+)".*?<span class="cat">(.*?)</span>(.*?)</p>'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedurl, scrapedtitle, scrapedthumbnail, categoria, info in matches:
            titulo = scrapertools.decodeHtmlentities(scrapedtitle)
            scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.split("[")[0])
            action = "findvideos"
            show = ""
            if "Series" in categoria:
                action = "episodios"
                show = scrapedtitle
            elif categoria and categoria != "peliculas" and categoria != "documentales":
                try:
                    titulo += " ["+categoria.rsplit(", ",1)[1]+"]"
                except:
                    titulo += " ["+categoria+"]"
                if 'l-espmini' in info:
                    titulo += " [ESP]"
                if 'l-latmini' in info:
                    titulo += " [LAT]"
                if 'l-vosemini' in info:
                    titulo += " [VOSE]"
            if not scrapedthumbnail.startswith("http"):
                scrapedthumbnail = "http:"+scrapedthumbnail
            scrapedthumbnail = scrapedthumbnail.replace("-129x180", "")
            scrapedthumbnail = scrapedthumbnail.rsplit("/", 1)[0]+"/"+urllib.quote(scrapedthumbnail.rsplit("/", 1)[1])
            if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
            itemlist.append(item.clone(action=action, title=titulo, url=scrapedurl, thumbnail=scrapedthumbnail,
                                       fulltitle=scrapedtitle, context=["buscar_trailer"], contentTitle=scrapedtitle,
                                       viewmode="movie_with_plot", show=show, contentType="movie"))

    #Paginación
    next_page = scrapertools.find_single_match(data, '<a class="nextpostslink".*?href="([^"]+)"')
    if next_page != "":
        itemlist.append(item.clone(title=">> Siguiente", url=next_page, text_color=color3))

    return itemlist


def generos(item):
    logger.info("pelisalacarta.channels.descargasmix generos")
    itemlist = []

    data = scrapertools.downloadpage(item.url)
    bloque = scrapertools.find_single_match(data, '<div class="categorias">(.*?)</div>')
    matches = scrapertools.find_multiple_matches(bloque, '<a href="([^"]+)">([^<]+)</a>')
    for scrapedurl, scrapedtitle in matches:
        scrapedurl = "http://desmix.net" + scrapedurl
        itemlist.append(item.clone(action="entradas", url=scrapedurl, title=scrapedtitle))

    return itemlist


def episodios(item):
    logger.info("pelisalacarta.channels.descargasmix episodios")
    itemlist = []

    data = scrapertools.downloadpage(item.url)
    patron = '(<ul class="menu" id="seasons-list">.*?<div class="section-box related-posts">)'
    bloque = scrapertools.find_single_match(data, patron)
    matches = scrapertools.find_multiple_matches(bloque, '<div class="cap">(.*?)</div>')
    for scrapedtitle in matches:
        scrapedtitle = scrapedtitle.strip()
        new_item = item.clone()
        new_item.infoLabels['season'] = scrapedtitle.split(" ", 1)[0].split("x")[0]
        new_item.infoLabels['episode'] = scrapedtitle.split(" ", 1)[0].split("x")[1]
        if item.fulltitle != "Añadir esta serie a la biblioteca":
            title = item.fulltitle+" "+scrapedtitle.strip()
        else:
            title = scrapedtitle.strip()
        itemlist.append(new_item.clone(action="findvideos", title=title, extra=scrapedtitle, fulltitle=title, contentType="episode"))

    itemlist.sort(key=lambda item: item.title, reverse=True)
    item.plot = scrapertools.find_single_match(data, '<strong>SINOPSIS</strong>:(.*?)</p>')
    if item.show != "" and item.extra == "":
        itemlist.append(item.clone(channel="trailertools", title="Buscar Tráiler", action="buscartrailer", context="",
                                   text_color="magenta"))
        if config.get_library_support():
            itemlist.append(Item(channel=item.channel, title="Añadir esta serie a la biblioteca", url=item.url,
                                 action="add_serie_to_library", extra="episodios", show=item.show,
                                 text_color="green"))

        try:
            from core import tmdb
            tmdb.set_infoLabels_itemlist(itemlist[:-2], __modo_grafico__)
        except:
            pass

    return itemlist


def epienlaces(item):
    logger.info("pelisalacarta.channels.descargasmix epienlaces")
    itemlist = []
    item.text_color = color3
    
    data = scrapertools.downloadpage(item.url)
    data = data.replace("\n", "").replace("\t", "")

    #Bloque de enlaces
    delimitador = item.extra.strip()
    delimitador = re.sub(r'(?i)(\[(?:/|)Color.*?\])', '', delimitador)
    patron = '<div class="cap">'+delimitador+'(.*?)(?:<div class="polo"|</li>)'
    bloque = scrapertools.find_single_match(data, patron)
     
    patron = '<div class="episode-server">.*?href="([^"]+)"' \
             '.*?data-server="([^"]+)"' \
             '.*?<div class="caliycola">(.*?)</div>'
    matches = scrapertools.find_multiple_matches(bloque, patron)

    itemlist.append(item.clone(action="", title="Enlaces de Descarga/Online", text_color=color1))
    for scrapedurl, scrapedserver, scrapedcalidad in matches:
        if scrapedserver == "ul":
            scrapedserver = "uploadedto"
        if scrapedserver == "streamin":
            scrapedserver = "streaminto"
        titulo = "    " + scrapedserver.capitalize() + " [" + scrapedcalidad + "]"
        #Enlaces descarga
        if scrapedserver == "magnet":
            itemlist.insert(0, item.clone(action="play", title=titulo, server="torrent", url=scrapedurl))
        else:
            mostrar_server = True
            if config.get_setting("hidepremium") == "true":
                mostrar_server = servertools.is_server_enabled(scrapedserver)
            if mostrar_server:
                try:
                    servers_module = __import__("servers."+scrapedserver)
                    if "enlacesmix.com" in scrapedurl:
                        itemlist.append(item.clone(action="play", title=titulo, server=scrapedserver, url=scrapedurl,
                                                   extra=item.url))
                    else:
                        enlaces = servertools.findvideos(data=scrapedurl)
                        if len(enlaces) > 0:
                            titulo = "    " + enlaces[0][2].capitalize() + "  [" + scrapedcalidad + "]"
                            itemlist.append(item.clone(action="play", server=enlaces[0][2], title=titulo,
                                                       url=enlaces[0][1]))
                except:
                    pass

    if itemlist[0].server == "torrent":
        itemlist.insert(0, item.clone(action="", title="Enlaces Torrent", text_color=color1))

    return itemlist


def findvideos(item):
    logger.info("pelisalacarta.channels.descargasmix findvideos")
    if item.extra and item.extra != "findvideos":
        return epienlaces(item)
    itemlist = []
    item.text_color = color3
    data = scrapertools.downloadpage(item.url)

    item.plot = scrapertools.find_single_match(data, 'SINOPSIS(?:</span>|</strong>):(.*?)</p>')
    year = scrapertools.find_single_match(data, '(?:<span class="bold">|<strong>)AÑO(?:</span>|</strong>):\s*(\d+)')
    if year != "":
        try:
            from core import tmdb
            item.infoLabels['year'] = year
            tmdb.set_infoLabels_item(item, __modo_grafico__)
        except:
            pass

    old_format = False
    #Patron torrent antiguo formato
    if "Enlaces de descarga</div>" in data:
        old_format = True
        matches = scrapertools.find_multiple_matches(data, 'class="separate3 magnet".*?href="([^"]+)"')
        for scrapedurl in matches:
            title = "[Torrent] "
            title += urllib.unquote(scrapertools.find_single_match(scrapedurl, 'dn=(.*?)(?i)WWW.DescargasMix'))
            itemlist.append(item.clone(action="play", server="torrent", title=title, url=scrapedurl, text_color="green"))
    
    #Patron online
    data_online = scrapertools.find_single_match(data, 'Ver online</div>(.*?)<div class="section-box related-'
                                                       'posts">')
    if len(data_online) > 0:
        title = "Enlaces Online"
        if '"l-latino2"' in data_online:
            title += " [LAT]"
        elif '"l-esp2"' in data_online:
            title += " [ESP]"
        elif '"l-vose2"' in data_online:
            title += " [VOSE]"
        itemlist.append(item.clone(title=title, action="", text_color=color1))
        patron = 'make_links.*?,[\'"]([^"\']+)["\']'
        matches = scrapertools.find_multiple_matches(data_online, patron)
        for code in matches:
            enlace = mostrar_enlaces(code)
            enlaces = servertools.findvideos(data=enlace[0])
            if len(enlaces) > 0:
                title = "   Ver vídeo en " + enlaces[0][2]
                itemlist.append(item.clone(action="play", server=enlaces[0][2], title=title, url=enlaces[0][1]))
    scriptg = scrapertools.find_single_match(data, "<script type='text/javascript'>str='([^']+)'")
    if scriptg:
        gvideo = urllib.unquote_plus(scriptg.replace("@", "%"))
        url = scrapertools.find_single_match(gvideo, 'src="([^"]+)"')
        if url:
            itemlist.append(item.clone(action="play", server="directo", url=url, title="   Ver vídeo en Googlevideo (Máxima calidad)", extra=item.url))

    #Patron descarga
    patron = '<div class="(?:floatLeft |)double(?:nuevo|)">(.*?)</div>(.*?)' \
             '(?:<div(?: id="mirrors"|) class="(?:contentModuleSmall |)mirrors">|<div class="section-box related-posts">)'
    bloques_descarga = scrapertools.find_multiple_matches(data, patron)
    for title_bloque, bloque in bloques_descarga:
        if title_bloque == "Ver online":
            continue
        if '"l-latino2"' in bloque:
            title_bloque += " [LAT]"
        elif '"l-esp2"' in bloque:
            title_bloque += " [ESP]"
        elif '"l-vose2"' in bloque:
            title_bloque += " [VOSE]"
        itemlist.append(item.clone(title=title_bloque, action="", text_color=color1))
        if '<div class="subiendo">' in bloque:
            itemlist.append(item.clone(title="   Los enlaces se están subiendo", action=""))
            continue
        patron = 'class="separate.*? ([^"]+)".*?(?:make_links.*?,|href=)[\'"]([^"\']+)["\']'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedserver, scrapedurl in matches:
            if (scrapedserver == "ul") | (scrapedserver == "uploaded"):
                scrapedserver = "uploadedto"
            titulo = scrapedserver.capitalize()
            if titulo == "Magnet" and old_format:
                continue
            elif titulo == "Magnet" and not old_format:
                title = "   Enlace Torrent"
                itemlist.append(item.clone(action="play", server="torrent", title=title, url=scrapedurl, text_color="green"))
                continue
            mostrar_server = True
            if config.get_setting("hidepremium") == "true":
                mostrar_server = servertools.is_server_enabled(scrapedserver)
            if mostrar_server:
                try:
                    servers_module = __import__("servers."+scrapedserver)
                    #Saca numero de enlaces
                    urls = mostrar_enlaces(scrapedurl)
                    numero = str(len(urls))
                    titulo = "   "+titulo+" - Nº enlaces:"+numero
                    itemlist.append(item.clone(action="enlaces", title=titulo, extra=scrapedurl))
                except:
                    pass

    itemlist.append(item.clone(channel="trailertools", title="Buscar Tráiler", action="buscartrailer", context="",
                               text_color="magenta"))
    if item.extra != "findvideos" and config.get_library_support():
        itemlist.append(Item(channel=item.channel, title="Añadir a la biblioteca", action="add_pelicula_to_library",
                             extra="findvideos", url=item.url, infoLabels={'title': item.fulltitle},
                             fulltitle=item.fulltitle, text_color="green"))

    return itemlist


def play(item):
    logger.info("pelisalacarta.channels.descargasmix play")
    itemlist = []
    if "enlacesmix.com" in item.url:
        DEFAULT_HEADERS.append(["Referer", item.extra])
        if not item.url.startswith("http:"):
            item.url = "http:" + item.url
        data = scrapertools.downloadpage(item.url, headers=DEFAULT_HEADERS)
        item.url = scrapertools.find_single_match(data, 'iframe src="([^"]+)"')
         
        enlaces = servertools.findvideos(data=item.url)[0]
        if len(enlaces) > 0:
            itemlist.append(item.clone(action="play", server=enlaces[2], url=enlaces[1]))
    elif item.server == "directo":
        global DEFAULT_HEADERS
        DEFAULT_HEADERS.append(["Referer", item.extra])
        data = scrapertools.downloadpage(item.url, headers=DEFAULT_HEADERS)
        subtitulo = scrapertools.find_single_match(data, "var subtitulo='([^']+)'")
        DEFAULT_HEADERS[1][1] = item.url
        calidades = ["1080p", "720p", "480p", "360p"]
        for i in range(0, len(calidades)):
            url_redirect = scrapertools.find_single_match(data, "{file:'([^']+)',label:'"+calidades[i]+"'")
            if url_redirect:
                url_video = scrapertools.get_header_from_response(url_redirect, header_to_get="location", headers=DEFAULT_HEADERS)
                if url_video:
                    url_video = url_video.replace(",", "%2C")
                    itemlist.append(item.clone(url=url_video, subtitle=subtitulo))
                    break
    else:
        itemlist.append(item.clone())
    
    return itemlist


def enlaces(item):
    logger.info("pelisalacarta.channels.descargasmix enlaces")
    itemlist = []
    data = scrapertools.downloadpage(item.url)

    urls = mostrar_enlaces(item.extra)
    numero = len(urls)
    for enlace in urls:
        enlaces = servertools.findvideos(data=enlace)
        if len(enlaces) > 0:
            for link in enlaces:
                if "/folder/" in enlace:
                    titulo = link[0]
                else:
                    titulo = item.title.split("-")[0]+" - Enlace "+str(numero)
                    numero -= 1
                itemlist.append(item.clone(action="play", server=link[2], title=titulo, url=link[1]))

    itemlist.sort(key=lambda item: item.title)
    return itemlist


def mostrar_enlaces(data):
    import base64
    data = data.split(",")
    len_data = len(data)
    urls = []
    for i in range (0, len_data):
        url = []
        value1 = base64.b64decode(data[i])
        value2 = value1.split("-")
        for j in range (0, len(value2)):
            url.append(chr(int(value2[j])))

        urls.append("".join(url))

    return urls
