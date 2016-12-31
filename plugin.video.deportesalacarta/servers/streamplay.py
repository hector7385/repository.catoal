# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para streamplay
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import re

from jjdecode import JJDecoder
from core import jsunpack
from core import logger
from core import scrapertools


def test_video_exists( page_url ):
    logger.info("deportesalacarta.streamplay test_video_exists(page_url='%s')" % page_url)
    data = scrapertools.cache_page(page_url)
    if data == "File was deleted":
        return False, "[Streamplay] El archivo no existe o ha sido borrado"

    return True, ""


def get_video_url( page_url , premium = False , user="" , password="", video_password="" ):
    logger.info("deportesalacarta.streamplay get_video_url(page_url='%s')" % page_url)
    data = scrapertools.cache_page(page_url)

    jj_encode = scrapertools.find_single_match(data, "(\w+=~\[\];.*?\)\(\)\)\(\);)")
    jj_decode = None
    jj_patron = None
    if jj_encode:
        jj_decode = JJDecoder(jj_encode).decode()
    if jj_decode:
        jj_patron = scrapertools.find_single_match(jj_decode, "/([^/]+)/")

    matches = scrapertools.find_single_match(data, "<script type=[\"']text/javascript[\"']>(eval.*?)</script>")
    matchjs = jsunpack.unpack(matches).replace("\\", "")

    matches = scrapertools.find_multiple_matches(matchjs, ',file:"([^"]+)"')
    video_urls = []
    for mediaurl in matches:
        filename = scrapertools.get_filename_from_url(mediaurl)[-4:]
        if mediaurl.startswith("rtmp"):
            rtmp, playpath = mediaurl.split("vod/", 1)
            mediaurl = "%svod/ playpath=%s pageUrl=%s" % (rtmp, playpath, page_url)
            filename = "rtmp"
        mediaurl = re.sub(r'%s' % jj_patron, r'\1', mediaurl)
        video_urls.append([filename + " [streamplay]", mediaurl])

    video_urls.sort(key=lambda x:x[0], reverse=True)
    for video_url in video_urls:
        logger.info("[streamplay.py] %s - %s" % (video_url[0], video_url[1]))

    return video_urls


# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    # http://streamplay.to/ubhrqw1drwlx
    patronvideos = "streamplay.to/(?:embed-|)([a-z0-9]+)(?:.html|)"
    logger.info("deportesalacarta.streamplay find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos, re.DOTALL).findall(data)

    for match in matches:
        titulo = "[streamplay]"
        url = "http://streamplay.to/embed-%s.html" % match
        if url not in encontrados:
            logger.info("  url="+url)
            devuelve.append([titulo, url, 'streamplay'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    return devuelve
