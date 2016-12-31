# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para BoxingClub
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import re, urllib
from core import logger
from core import config
from core import scrapertools
from core import servertools
from core.item import Item

__channel__ = "boxingclub"


DEBUG = config.get_setting("debug")
host = "http://www.pokeryour.ru"
headers= [['User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0']]


def mainlist(item):
    logger.info("deportesalacarta.channels.boxingclub mainlist")
    itemlist = []

    itemlist.append(Item(channel=__channel__, title="[COLOR green]Novedades[/COLOR]", url="https://www.reddit.com/r/OrganizedViolence/new/", action="novedades", thumbnail=item.thumbnail, fanart=item.fanart))
    itemlist.append(Item(channel=__channel__, title="[COLOR green]Boxeo[/COLOR]", url="http://www.pokeryour.ru/sport/categories/8-boxing.html", action="novedades_pokeryour", thumbnail="http://i.imgur.com/zkmHvUo.jpg?1", fanart=item.fanart))
    itemlist.append(Item(channel=__channel__, title="[COLOR green]MMA[/COLOR]", url="http://www.pokeryour.ru/sport/categories/22-mma.html", action="novedades_pokeryour", thumbnail="http://i.imgur.com/pVwNLDx.jpg?1", fanart=item.fanart))
    itemlist.append(Item(channel=__channel__, title="[COLOR green]UFC[/COLOR]", url="http://mmaversus.com/category/fight-videos-2/", action="ufc", thumbnail="http://i.imgur.com/iokwVlI.jpg?1", fanart=item.fanart))
    itemlist.append(Item(channel=__channel__, title="[COLOR green]WWE[/COLOR]", url="http://watchwrestling.uno/", action="wwe", thumbnail="http://i.imgur.com/Czjl5HA.jpg?1", fanart="http://i.imgur.com/iRYYRuB.jpg"))
    itemlist.append(Item(channel=__channel__, title="[COLOR green]Buscar...[/COLOR]", url="", action="search", thumbnail=item.thumbnail, fanart=item.fanart))

    return itemlist


def novedades(item):
    logger.info("deportesalacarta.channels.boxingclub novedades")
    itemlist = []
    data = scrapertools.cachePage(item.url)
    data = re.sub(r"\n|\r|\t", '', data)

    bloque_entradas = scrapertools.find_multiple_matches(data, '<div class=" thing(.*?)<div class="child"')
    for bloque in bloque_entradas:
        if "thumbnail default may-blank" in bloque:
            patron = 'data-url="([^"]+)".*?(thumbnail default may-blank).*?tabindex.*?>(.*?)</a>'
        else:
            patron = 'data-url="([^"]+)".*?src="([^"]+)".*?tabindex.*?>(.*?)</a>'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedurl, scrapedthumbnail, scrapedtitle in matches:
            if scrapedthumbnail == "thumbnail default may-blank": scrapedthumbnail = item.thumbnail
            else: scrapedthumbnail = "http:" + scrapedthumbnail
            date = scrapertools.find_single_match(scrapedtitle, '([\d]+/[\d]+/[\d]+)')
            if date != "":
                month, day, year = scrapertools.find_single_match(date, '([\d]+)/([\d]+)/([\d]+)')
                scrapedtitle = scrapedtitle.replace(date, day+"/"+month+"/"+year)
            scrapedtitle = scrapedtitle.replace("[Boxing]","[Boxeo]")
            scrapedtitle = "[COLOR darkorange]"+scrapedtitle.split("]",1)[0]+"][/COLOR][COLOR red]"+scrapedtitle.split("]",1)[1]+"[/COLOR]"
            if "youtu.be" in scrapedurl:
                scrapedurl = scrapedurl.replace("youtu.be/","www.youtube.com/watch?v=")
            itemlist.append(Item(channel=__channel__, title=scrapedtitle, action="play", url=scrapedurl, thumbnail=scrapedthumbnail, folder=False))
    
    next_page = scrapertools.find_single_match(data, '<a href="([^"]+)" rel="nofollow next"')
    if next_page != "":
        itemlist.append(Item(channel=__channel__, title=">> Siguiente", action="novedades", url=next_page, thumbnail=item.thumbnail, folder=True))
    return itemlist


def search(item, texto):
    logger.info("deportesalacarta.channels.boxingclub search")
    item.url = "https://www.reddit.com/r/OrganizedViolence/search?q=%s&sort=new&restrict_sr=on" % texto
    itemlist = busqueda(item)
    return itemlist


def busqueda(item):
    logger.info("deportesalacarta.channels.boxingclub busqueda")
    itemlist = []
    data = scrapertools.cachePage(item.url)
    data = re.sub(r"\n|\r|\t", '', data)
    
    bloque_entradas = scrapertools.find_multiple_matches(data, '<div class=" search-result search-result-link(.*?)<\/div><\/div>')
    for bloque in bloque_entradas:
        if 'may-blank thumbnail default' in bloque:
            patron = '(may-blank thumbnail default).*?class="search-title may-blank" >(.*?)</a>.*?class="search-link may-blank" >(.*?)</a>'
        else:
            patron = 'src="([^"]+)".*?class="search-title may-blank" >(.*?)</a>.*?class="search-link may-blank" >(.*?)</a>'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedthumbnail, scrapedtitle, scrapedurl in matches:
            if scrapedthumbnail == "may-blank thumbnail default": scrapedthumbnail = item.thumbnail
            else: scrapedthumbnail = "http:" + scrapedthumbnail
            date = scrapertools.find_single_match(scrapedtitle, '([\d]+/[\d]+/[\d]+)')
            if date != "":
                month, day, year = scrapertools.find_single_match(date, '([\d]+)/([\d]+)/([\d]+)')
                scrapedtitle = scrapedtitle.replace(date, day+"/"+month+"/"+year)
            scrapedtitle = scrapedtitle.replace("[Boxing]","[Boxeo]")
            scrapedtitle = "[COLOR darkorange]"+scrapedtitle.split("]",1)[0]+"][/COLOR][COLOR red]"+scrapedtitle.split("]",1)[1]+"[/COLOR]"
            if "youtu.be" in scrapedurl:
                scrapedurl = scrapedurl.replace("youtu.be/","www.youtube.com/watch?v=")
            itemlist.append(Item(channel=__channel__, title=scrapedtitle, action="play", url=scrapedurl, thumbnail=scrapedthumbnail, folder=False))
    
    next_page = scrapertools.find_single_match(data, '<a href="([^"]+)" rel="nofollow next"')
    if next_page != "":
        itemlist.append(Item(channel=__channel__, title=">> Siguiente", action="busqueda", url=next_page, thumbnail=item.thumbnail, folder=True))
    return itemlist


def novedades_pokeryour(item):
    logger.info("deportesalacarta.channels.boxingclub novedades_pokeryour")
    itemlist = []
    ## Petición 1
    url = "http://translate.google.com/translate?depth=1&nv=1&rurl=translate.google.com&sl=ru&tl=es&u="+item.url
    data = scrapertools.decodeHtmlentities( scrapertools.downloadpage(url,follow_redirects=False) )
    ## Petición 2
    url = scrapertools.get_match(data, ' src="([^"]+)" name=c ')
    data = scrapertools.decodeHtmlentities( scrapertools.downloadpage(url,follow_redirects=False) )
    ## Petición 3
    url = scrapertools.get_match(data, 'URL=([^"]+)"')
    data = scrapertools.decodeHtmlentities( scrapertools.cachePage(url) )
    data = re.sub(r"\n|\r|\t|</span> comentario de Rusia.</span>", '', data)

    bloque_entradas = scrapertools.find_multiple_matches(data, '<div class="item column(.*?)<div class=item-separator>')
    for bloque in bloque_entradas:
        patron = 'title="([^>]+)>.*?<a href=([^>]+)>.*?' \
                 '<img src=(/sport/media/com_hwdmediashare/files/[^\s]+).*?' \
                 '<dd class=media-info-description>.*?</span>(.*?)</span>'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for scrapedtitle, scrapedurl, scrapedthumbnail, scrapedplot  in matches:
            scrapedthumbnail = host + scrapedthumbnail

            scrapedtitle = scrapedtitle.replace("vídeo de alta definición","HD").replace('::"','')
            scrapedtitle = re.sub(r'(?i)- tarjeta principal|tarjeta de|tarjeta|en línea de|el vídeo|el video|vídeo|video|en línea|en ruso|::','',scrapedtitle)
            if not "/" in scrapedtitle: scrapedtitle += "/"
            scrapedtitle = "[COLOR darkorange]"+scrapedtitle.split("/",1)[0]+"/[/COLOR][COLOR red]"+scrapedtitle.split("/",1)[1]+"[/COLOR]"
            scrapedurl = scrapedurl.replace("http://translate.googleusercontent.com/translate_c?depth=2&nv=1&rurl=translate.google.com&sl=ru&tl=es&u=","")
            scrapedurl = urllib.unquote(scrapedurl)
            itemlist.append(Item(channel=__channel__, title=scrapedtitle, action="play", url=scrapedurl, thumbnail=scrapedthumbnail, plot=scrapedplot, folder=True))
    
    next_page = scrapertools.find_single_match(data, '<li class=pagination-next>.*?href=([^\s]+)')
    if next_page != "":
        itemlist.append(Item(channel=__channel__, title=">> Siguiente", action="novedades_pokeryour", url=next_page, thumbnail=item.thumbnail, folder=True))
    return itemlist


def ufc(item):
    logger.info("deportesalacarta.channels.boxingclub ufc")
    itemlist = []
    data = scrapertools.cachePage(item.url)
    data = re.sub(r"\n|\r|\t", '', data)

    patron = '<div class="thumbnail overlay">.*?src="([^"]+)".*?' \
             '<h3>.*?<a href="([^"]+)">(.*?)</a>.*?' \
             '<div class="entry-excerpt">.*?<p>(.*?)</p>'
    matches = scrapertools.find_multiple_matches(data, patron)
    for scrapedthumbnail, scrapedurl, scrapedtitle, scrapedplot in matches:
        scrapedthumbnail = scrapedthumbnail.replace("-425x225","")+"|Referer="+item.url
        scrapedtitle = scrapedtitle.replace("Fight Video","")
        scrapedtitle = "[COLOR darkorange]"+scrapedtitle+"[/COLOR]"
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, action="play", url=scrapedurl, thumbnail=scrapedthumbnail, folder=False))
    
    next_page = scrapertools.find_single_match(data, '<a class="next page-numbers" href="([^"]+)"')
    if next_page != "":
        itemlist.append(Item(channel=__channel__, title=">> Siguiente", action="ufc", url=next_page, thumbnail=item.thumbnail, folder=True))
    return itemlist


def wwe(item):
    logger.info("deportesalacarta.channels.boxingclub wwe")
    itemlist = []
    data = scrapertools.cachePage(item.url)
    data = re.sub(r"\n|\r|\t", '', data)
    bloque = scrapertools.find_single_match(data, '<ul class="sub-menu">(.*?)</div>')
    patron = '<a href="([^"]+)">(.*?)</a>'
    matches = scrapertools.find_multiple_matches(bloque, patron)
    urls = []
    for scrapedurl, scrapedtitle in matches:
        if "Live" in scrapedtitle: continue
        if not scrapedurl in urls:
            urls.append(scrapedurl)
        else: continue
        scrapedtitle = scrapedtitle.replace("Others","Otros")
        if len(itemlist) % 2 == 0:
            scrapedtitle= "[COLOR green]%s[/COLOR]" % scrapedtitle
        else: scrapedtitle= "[COLOR darkorange]%s[/COLOR]" % scrapedtitle
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="wwe_entradas", thumbnail=item.thumbnail, fanart=item.fanart))

    return itemlist


def wwe_entradas(item):
    logger.info("deportesalacarta.channels.boxingclub wwe_entradas")
    itemlist = []
    data = scrapertools.cachePage(item.url)
    data = re.sub(r"\n|\r|\t", '', data)
    patron = '<div id="post-.*?title="([^"]+)".*?href="([^"]+)".*?' \
             'src="([^"]+)".*?entry-summary">(.*?)</p>'
    matches = scrapertools.find_multiple_matches(data, patron)
    for scrapedtitle, scrapedurl, scrapedthumbnail, scrapedplot in matches:
        scrapedtitle = re.sub(r'(?i)full|show|online|free','',scrapedtitle).strip()
        try:
            fecha, mes, dia, year = scrapertools.find_single_match(scrapedtitle, '((\d+)/(\d+)/(\d+))')
            fecha_string = "[COLOR darkorange]"+dia+"/"+mes+"/"+year+"[/COLOR]"
            scrapedtitle = scrapedtitle.replace(fecha, fecha_string)
            scrapedtitle = "[COLOR green]"+scrapedtitle.split(fecha)[0]+"[/COLOR] "+scrapedtitle.split(fecha)[1]+fecha_string
        except:
            scrapedtitle = "[COLOR green]"+scrapedtitle+"[/COLOR]"
            pass

        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="findvideos", thumbnail=scrapedthumbnail, plot=scrapedplot, folder=True))

    next_page = scrapertools.find_single_match(data, '<a class="nextpostslink" rel="next" href="([^"]+)"')
    if next_page != "":
        itemlist.append(Item(channel=__channel__, title=">> Siguiente", url=next_page, action="wwe_entradas", thumbnail=item.thumbnail, folder=True))

    return itemlist


def findvideos(item):
    logger.info("deportesalacarta.channels.boxingclub findvideos")
    itemlist = []
    
    if item.extra == "":
        data = scrapertools.cachePage(item.url)
        data = re.sub(r"\n|\r|\t", '', data)
        matches = scrapertools.find_multiple_matches(data, '">(\w+)[^<]+<\/p><p style="text-align: center;">(.*?)(?:3px;|<p class="no-break">)')
        for server, enlaces in matches:
            try:
                server = server.replace("VIDTO","vidtome").replace("MOVHSARE","movshare").lower()
                if server != "download":
                    servers_module = __import__("servers."+server)
                    title = "[COLOR indianred]Enlaces en [/COLOR][COLOR darkorange]"+server.capitalize()+"[/COLOR]"
                else: title = "[COLOR indianred]Enlaces de [/COLOR][COLOR darkorange]Descarga[/COLOR]"
                itemlist.append(Item(channel=__channel__, title=title, url=item.url, action="findvideos", server=server, thumbnail=item.thumbnail, plot=item.plot, extra=enlaces, referer=item.url, folder=True))
            except:
                pass
    else:
        matches = scrapertools.find_multiple_matches(item.extra, 'a href="([^"]+)".*?>([^<]+)<')
        for scrapedurl, scrapedtitle in matches:
            if "Descarga" in item.title:
                try:
                    server = re.sub(r'(?i)uploaded','uploadedto', scrapedtitle)
                    servers_module = __import__("servers."+server.lower())
                    scrapedtitle = "[COLOR indianred]Descarga en [/COLOR][COLOR darkorange]"+scrapedtitle+"[/COLOR]"
                    itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="play", server=server.lower(), thumbnail=item.thumbnail, plot=item.plot, folder=False))
                except:
                    pass
            else:
                scrapedtitle = "[COLOR indianred]"+scrapedtitle+"[/COLOR] [COLOR darkorange]["+item.server+"][/COLOR]"
                if "Protect" in scrapedurl: scrapedurl = "http://prowrestlingreports.com/cgi-bin/%s" % scrapedurl
                itemlist.append(Item(channel=__channel__, title=scrapedtitle, url=scrapedurl, action="play", server=item.server, thumbnail=item.thumbnail, plot=item.plot, referer=item.referer, folder=False))

    return itemlist


def play(item):
    logger.info("deportesalacarta.channels.boxingclub play")
    itemlist = []
    if "pokeryou" in item.url:
        data = scrapertools.cachePage(item.url)
        docid = scrapertools.find_single_match(data, 'docid=([^&]+)&')
        url = "https://docs.google.com/get_video_info?docid=%s&eurl=%s&authuser=" % (docid, item.url)
        data = scrapertools.cachePage(url).decode('unicode-escape')
        data = urllib.unquote(data)
        url = scrapertools.find_single_match(data, 'fmt_stream_map.*?(https.*?),')
        video_url = url.decode('unicode-escape')
        itemlist.append( Item(channel=__channel__ , action="play" , server="directo", title=item.title, url=video_url, thumbnail=item.thumbnail, folder=False))
    elif "mmatd.com" in item.url:
        data = scrapertools.cachePage(item.url)
        video_url = scrapertools.find_single_match(data, 'file: "([^"]+)"')
        itemlist.append( Item(channel=__channel__ , action="play" , server="directo", title=item.title, url=video_url, thumbnail=item.thumbnail, folder=False))
    elif "mmaversus" in item.url:
        data = scrapertools.cachePage(item.url)
        url_redirect = scrapertools.find_single_match(data, '<a href="(http://bestinmma[^"]+)"')
        data = scrapertools.cachePage(url_redirect)
        video_itemlist = servertools.find_video_items(data=data)
        for video_item in video_itemlist:
            itemlist.append( Item(channel=__channel__ , action="play" , server=video_item.server, title=video_item.title, url=video_item.url, thumbnail=item.thumbnail, fanart=item.fanart, folder=False))       
    elif "prowrestlingreports" in item.url:
        headers.append(['Referer',item.referer])
        data = scrapertools.cachePage(item.url, headers=headers)
        logger.info(data)
        url = scrapertools.find_single_match(data, '<iframe src="([^"]+)"')
        itemlist.append( Item(channel=__channel__ , action="play" , server=item.server, title=item.title, url=url, thumbnail=item.thumbnail, fanart=item.fanart, folder=False))             
    else:
        video_itemlist = servertools.find_video_items(data=item.url)
        for video_item in video_itemlist:
            itemlist.append( Item(channel=__channel__ , action="play" , server=video_item.server, title=video_item.title, url=video_item.url, thumbnail=item.thumbnail, fanart=item.fanart, folder=False))       
    
    return itemlist
