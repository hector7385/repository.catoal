# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta 4
# Copyright 2015 tvalacarta@gmail.com
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# This file is part of pelisalacarta 4.
#
# pelisalacarta 4 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pelisalacarta 4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pelisalacarta 4.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------
# Updater
# --------------------------------------------------------------------------------

import os
import re
import time
import urllib2
import xbmc

import config
import downloadtools
import logger
import filetools
import scrapertools
from platformcode import platformtools

REMOTE_VERSION_FILE = "https://raw.githubusercontent.com/CmosGit/Mod_pelisalacarta_deportes/addon/version.xml"
LOCAL_XML_FILE = os.path.join(config.get_runtime_path() , "version.xml" )


def check():
    logger.info("deportesalacarta.channels.update_sports Comprobando versión")
    try:
        data = scrapertools.downloadpage(REMOTE_VERSION_FILE)
        version_publicada = scrapertools.find_single_match(data,"<version>([^<]+)</version>").strip()
        message = scrapertools.find_single_match(data,"<changes>([^<]+)</changes>").strip()
        logger.info("deportesalacarta.channels.update_sports Versión en el repositorio: %s" % version_publicada)

        # Lee el fichero con la versión instalada
        fichero = open(LOCAL_XML_FILE, "r")
        data = fichero.read()
        fichero.close()
        version_local = scrapertools.find_single_match(data,"<version>([^<]+)</version>").strip()

        logger.info("deportesalacarta.channels.update_sports Versión local: %s" % version_local)
        if float(version_publicada) > float(version_local):
            logger.info("deportesalacarta.channels.update_sports Nueva versión encontrada")
            return True, version_publicada, message
        else:
            logger.info("deportesalacarta.channels.update_sports No existe versión actualizada")
            return False, "", ""
    except:
        import traceback
        logger.error("deportesalacarta.platformcode.launcher "+traceback.format_exc())
        return False, "", ""


def actualiza(item):
    logger.info("deportesalacarta.channels.update_sports actualiza")

    local_folder = os.path.join(xbmc.translatePath("special://home"), "addons")
    error = False
    url = "https://github.com/CmosGit/Mod_pelisalacarta_deportes/raw/addon/plugin.video.deportesalacarta-%s.zip" % item.version
    progreso = platformtools.dialog_progress("Progreso de la actualización", "Descargando...")
    filename = 'deportesalacarta-%s.zip' % item.version
    localfilename = filetools.join(config.get_data_path(), filename)
    try:
        result = downloadtools.downloadfile(url, localfilename, continuar=True)
        progreso.update(50, "Descargando archivo", "Descargando...")
        # Lo descomprime
        logger.info("deportesalacarta.channels.configuracion descomprime fichero...")
        from core import ziptools
        unzipper = ziptools.ziptools()
        logger.info("deportesalacarta.channels.configuracion destpathname=%s" % local_folder)
        unzipper.extract(localfilename, local_folder, update=True)
        progreso.close()
    except:
        import traceback
        logger.info("Detalle del error: %s" % traceback.format_exc())
        # Borra el zip descargado
        filetools.remove(localfilename)
        progreso.close()
        platformtools.dialog_ok("Error", "Se ha producido un error extrayendo el archivo")
        return
    
    # Borra el zip descargado
    logger.info("deportesalacarta.channels.configuracion borra fichero...")
    filetools.remove(localfilename)
    logger.info("deportesalacarta.channels.configuracion ...fichero borrado")

    platformtools.dialog_ok("Actualizado correctamente", "Versión %s instalada con éxito" % item.version)
    
    xbmc.executebuiltin("Container.Refresh")
        

def do_download(url, localfilename):
    # Corregimos el filename para que se adapte al sistema en el que se ejecuta
    localfilename = os.path.normpath(localfilename)
    logger.info("deportesalacarta.channels.update_sports localfilename=%s" % localfilename)
    logger.info("deportesalacarta.channels.update_sports url=%s" % url)
    logger.info("deportesalacarta.channels.update_sports descarga fichero...")
    inicio = time.clock()
    
    error = False
    try:
        folder = os.path.dirname(localfilename)
        if not os.path.exists(folder):
            os.makedirs(folder)
        if os.path.exists(localfilename.rsplit(".",1)[0] + ".pyo"):
            os.remove(localfilename.rsplit(".",1)[0] + ".pyo")
        data = urllib2.urlopen(url).read()
        outfile = open(localfilename ,"wb")
        outfile.write(data)
        outfile.close()
        logger.info("deportesalacarta.channels.update_sports Grabado a " + localfilename)
         
    except:
        logger.info("deportesalacarta.channels.update_sports Error al grabar " + localfilename)
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line )
        error = True
    
    fin = time.clock()
    logger.info("deportesalacarta.channels.update_sports Descargado en %d segundos " % (fin-inicio+1))
    return error
