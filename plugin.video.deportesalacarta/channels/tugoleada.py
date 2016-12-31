# -*- coding: utf-8 -*-
#------------------------------------------------------------
# deportesalacarta - XBMC Plugin
# Canal para TUGOLEADA
# http://blog.tvalacarta.info/plugin-xbmc/deportesalacarta/
#------------------------------------------------------------
import re
import datetime

from core import scrapertools
from core import servertools
from core import logger
from core import config
from core.item import Item

__channel__ = "tugoleada"

host = "http://tumarcador.xyz/"


def mainlist(item):
    logger.info("deportesalacarta.channels.tugoleada mainlist")
    itemlist = []

    itemlist.append(Item(channel=__channel__, title="Agenda/Directos", action="entradas", url="http://www.elitegol.com", thumbnail="http://i.imgur.com/DegBUpj.png",fanart="http://i.imgur.com/bCn8lHB.jpg?1"))
    itemlist.append(Item(channel=__channel__, title="Canales Web/Html5", action="canales", url=host, thumbnail="http://i.imgur.com/DegBUpj.png",fanart="http://i.imgur.com/bCn8lHB.jpg?1"))

    return itemlist


def agendaglobal(item):
    itemlist = []
    try:
        item.channel = __channel__
        item.url = "http://www.elitegol.com"
        item.thumbnail="http://i.imgur.com/DegBUpj.png"
        item.fanart="http://i.imgur.com/bCn8lHB.jpg?1"
        itemlist = entradas(item)
        for item_global in itemlist:
            if item_global.action == "":
                itemlist.remove(item_global)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []

    return itemlist


def canales(item):
    logger.info("deportesalacarta.channels.tugoleada canales")
    itemlist = []

    data = scrapertools.downloadpage(item.url)
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)
    bloque = scrapertools.find_single_match(data, '<ul class="dropdown-menu"(.*?)</ul>')
    patron = '<a href="([^"]+)">(.*?)</a>'
    matches = scrapertools.find_multiple_matches(bloque, patron)

    for scrapedurl, scrapedtitle  in matches:
        scrapedurl = host + scrapedurl.replace("..", "")
        scrapedtitle = "[COLOR darkorange]"+scrapedtitle.strip()+"[/COLOR] [COLOR green]["+ \
                       item.title.replace('Canales ','')+"][/COLOR]"
        itemlist.append(Item(channel=__channel__, title=scrapedtitle, action="play", url=scrapedurl, thumbnail=item.thumbnail, fanart=item.fanart, folder=False))

    return itemlist


def entradas(item):
    logger.info("deportesalacarta.channels.tugoleada entradas")
    itemlist = []

    data = scrapertools.downloadpage(host)
    bloque = scrapertools.find_single_match(data, '<div class="col-md-12">(.*?)</div>')
    try:
        matches = scrapertools.find_multiple_matches(bloque, '(?i)<p.*?>(?:<img.*?>|)(.*?CANAL\s*(\d+))</p>')
        for scrapedtitle, canal in matches:
            url = host + "canal" + canal
            scrapedtitle = "[COLOR green]%s[/COLOR]" % scrapedtitle
            itemlist.append(item.clone(title=scrapedtitle, url=url, action="play"))
    except:
        import traceback
        logger.info(traceback.format_exc())
        matches = []
        
    if not itemlist:
        matches = scrapertools.find_multiple_matches(data, 'src="(https://i.gyazo.com[^"]+)"')
        for i, imagen in enumerate(matches):
            title = "Agenda: Imagen " + str(i+1) +" (Click para agrandar)"
            itemlist.append(item.clone(title=title, url=imagen, thumbnail=imagen, action="abrir_imagen", folder=False))
    
    if not matches and re.search(r"(?i)elitegol", data):
        data = scrapertools.downloadpage(item.url)
        data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)
        patron = '<div class="litd fecha">(.*?)\s*-\s*(\d+:\d+).*?</div>.*?src=".*?(\d+).png"' \
                 '.*?<div class="litd competicion">(.*?)</div>.*?href=[^>]+>(.*?)</a>' \
                 '.*?javascript:abrir_evento\((\d+)\)(.*?)</li>'
        matches = scrapertools.find_multiple_matches(data, patron)

        lista = []
        urls = []
        sports = {"1": "futbol", "2": "baloncesto", "3": "F1", "4": "tenis", "5": "ciclismo",
                  "6": "otro", "7": "béisbol", "8": "rugby", "9": "voleybol"}
        for fecha, hora, sport, torneo, evento, id, check_live  in matches:
            fecha = scrapertools.htmlclean(fecha)
            urls.append("http://www.elitegol.com/ajax/abrir_evento.php?id=%s" % id)
            partido = "[COLOR darkorange][B]"+evento+"[/B][/COLOR]"
            torneo = "  [COLOR blue]"+torneo+"[/COLOR]"
            if "EN JUEGO" in check_live: scrapedtitle = "[COLOR red][B]"+fecha+"-"+hora+"[/B][/COLOR] " + partido + torneo
            else: scrapedtitle = "[COLOR green][B]"+fecha+"-"+hora+"[/B][/COLOR] " + partido + torneo
            if re.search(r'(?i)hoy', fecha):
                date = datetime.datetime.today()
                date = date.strftime("%d/%m")
            elif re.search(r'(?i)mañana', fecha):
                date = datetime.datetime.today() + datetime.timedelta(days=1)
                date = date.strftime("%d/%m")
            else:
                date = fecha

            try:
                deporte = sports[sport]
            except:
                deporte = "otro"
            lista.append(Item(channel=__channel__, title=scrapedtitle, action="", url="", date=date, time=hora, deporte=deporte, evento=evento))

        try:
            from multiprocessing.dummy import Pool as ThreadPool
            thread = ThreadPool()
            results = thread.map(scrapertools.downloadpageWithoutCookies, urls)
            thread.close()
            thread.join()
        except:
            results = []
            for url_ajax in urls:
                data_result = scrapertools.downloadpageWithoutCookies(url_ajax)
                results.append(data_result)
        
        prox_eventos = []
        for i, data in enumerate(results):
            busqueda = re.search(r'(?i)tumarcador', data, flags=re.DOTALL)
            if busqueda:
                canal = scrapertools.find_single_match(data, '(?i)>(?:\w+|\s*|)tumarcador.*?(\d+).*?</a>')
                fulltitle = lista[i].fulltitle
                scrapedurl = host + "canal" + canal
                itemlist.append(lista[i].clone(action="play", url=scrapedurl))
            else:
                prox_eventos.append(lista[i])

        itemlist.append(Item(channel=__channel__, action="", title="", folder=False))            
        itemlist.append(Item(channel=__channel__, action="", title="[COLOR magenta][B]Posibles próximos eventos (No confirmados)[/B][/COLOR]", folder=False))
        for evento in prox_eventos:
            itemlist.append(evento)

    return itemlist


def abrir_imagen(item):
    import xbmc
    return xbmc.executebuiltin('ShowPicture('+item.url+')')


def play(item):
    itemlist = []
    data = scrapertools.downloadpage(item.url)
    if "Web" in item.title:
        videourl = scrapertools.find_single_match(data, "source: '([^']+)'")
        if not videourl:
            baseurl, var_url, lasturl = scrapertools.find_single_match(data, 'return\(\[([^\[]+)\].*?\+\s*([A-z]+)\.join.*?"([^"]+)"\)\.innerHTML')
            auth = scrapertools.find_single_match(data, var_url+'\s*=\s*\[([^\[]+)\]')
            lasturl = scrapertools.find_single_match(data, lasturl+'\s*>\s*([^<]+)<')
            videourl = baseurl + auth + lasturl
            videourl = re.sub(r'"|,|\\', '', videourl)
        itemlist.append(Item(channel=__channel__, title=item.title, server="directo", url=videourl, action="play", folder=False))
    else:
        lista = servertools.findvideosbyserver(data, 'p2p')
        if lista:
            itemlist.append(Item(channel=__channel__, title=item.title, server="p2p", url=lista[0][1], action="play", folder=False))
    return itemlist
