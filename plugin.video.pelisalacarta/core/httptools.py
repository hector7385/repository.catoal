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
# httptools
# --------------------------------------------------------------------------------
import urllib
import urllib2
import urlparse
import cookielib
import os
import time
from StringIO import StringIO
import gzip
from core import logger
from core import config
from threading import Lock

cookies_lock = Lock()


def downloadpage(url, post=None, headers=None, timeout=None, follow_redirects=True, cookies=True, replace_headers=False, add_referer=False, only_headers=False):
    """
    Abre una url y retorna los datos obtenidos

    @param url: url que abrir.
    @type url: str
    @param post: Si contiene algun valor este es enviado mediante POST.
    @type post: str
    @param headers: Headers para la petición, si no contiene nada se usara los headers por defecto.
    @type headers: dict, list
    @param timeout: Timeout para la petición.
    @type timeout: int
    @param follow_redirects: Indica si se han de seguir las redirecciones.
    @type follow_redirects: bool
    @param cookies: Indica si se han de usar las cookies.
    @type cookies: bool
    @param replace_headers: Si True, los headers pasados por el parametro "headers" sustituiran por completo los headers por defecto.
                            Si False, los headers pasados por el parametro "headers" modificaran los headers por defecto.
    @type replace_headers: bool
    @param add_referer: Indica si se ha de añadir el header "Referer" usando el dominio de la url como valor.
    @type add_referer: bool
    @param only_headers: Si Ture, solo se descargarán los headers, omitiendo el contenido de la url.
    @type only_headers: bool
    @return: Resultado de la petición
    @rtype: HTTPResponse

            Parametro               Tipo    Descripción
            ----------------------------------------------------------------------------------------------------------------
            HTTPResponse.sucess:    bool   True: Peticion realizada correctamente | False: Error al realizar la petición
            HTTPResponse.code:      int    Código de respuesta del servidor o código de error en caso de producirse un error
            HTTPResponse.error:     str    Descripción del error en caso de producirse un error
            HTTPResponse.headers:   dict   Diccionario con los headers de respuesta del servidor
            HTTPResponse.data:      str    Respuesta obtenida del servidor
            HTTPResponse.time:      float  Tiempo empleado para realizar la petición

    """

    response = {}

    # Headers por defecto, si no se especifica nada
    request_headers = dict()
    request_headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    request_headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    request_headers["Accept-Language"] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
    request_headers["Accept-Charset"] = "UTF-8"
    request_headers["Accept-Encoding"] = "gzip"

    # Headers pasados como parametros
    if headers is not None:
        if not replace_headers:
            request_headers.update(dict(headers))
        else:
            request_headers = dict(headers)
    
    if add_referer:
      request_headers["Referer"] = "/".join(url.split("/")[:3])
    
    url = urllib.quote(url, safe="%/:=&?~#+!$,;'@()*[]")

    ficherocookies = os.path.join(config.get_data_path(), "cookies.dat")

    logger.info("----------------------------------------------")
    logger.info("downloadpage")
    logger.info("----------------------------------------------")
    logger.info("Timeout: %s" % timeout)
    logger.info("URL: " + url)
    logger.info("Dominio: " + urlparse.urlparse(url)[1])
    if post:
        logger.info("Peticion: POST")
    else:
        logger.info("Peticion: GET")
    logger.info("Usar Cookies: %s" % cookies)
    logger.info("Descargar Pagina: %s" % (not only_headers))
    logger.info("Fichero de Cookies: " + ficherocookies)
    logger.info("Headers:")
    for header in request_headers:
        logger.info("- %s: %s" % (header, request_headers[header]))

    # Handlers
    handlers = [urllib2.HTTPHandler(debuglevel=False)]

    if not follow_redirects:
        handlers.append(NoRedirectHandler())

    cj = None
    if cookies:
        cj = cookielib.MozillaCookieJar()

        cookies_lock.acquire()
        if os.path.isfile(ficherocookies):
            logger.info("Leyendo fichero cookies")
            try:
                cj.load(ficherocookies, ignore_discard=True)
            except:
                logger.info("El fichero de cookies existe pero es ilegible, se borra")
                os.remove(ficherocookies)
        cookies_lock.release()

        handlers.append(urllib2.HTTPCookieProcessor(cj))

    opener = urllib2.build_opener(*handlers)

    logger.info("Realizando Peticion")

    # Contador
    inicio = time.time()

    req = urllib2.Request(url, post, request_headers)

    try:
        if urllib2.__version__ == "2.4":
            import socket
            deftimeout = socket.getdefaulttimeout()
            if timeout is not None:
                socket.setdefaulttimeout(timeout)
            handle = opener.open(req)
            socket.setdefaulttimeout(deftimeout)
        else:
            handle = opener.open(req, timeout=timeout)

    except urllib2.HTTPError, handle:
        response["sucess"] = False
        response["code"] = handle.code
        if "reason" in handle:
          response["error"] = handle.reason
        else:
          response["error"] = str(handle)
        response["headers"] = handle.headers.dict
        if not only_headers:
          response["data"] = handle.read()
        else:
          response["data"] = ""
        response["time"] = time.time() - inicio

    except Exception, e:
        response["sucess"] = False
        response["code"] = e.errno
        response["error"] = e.reason
        response["headers"] = {}
        response["data"] = ""
        response["time"] = time.time() - inicio

    else:
        response["sucess"] = True
        response["code"] = handle.code
        response["error"] = None
        response["headers"] = handle.headers.dict
        if not only_headers:
          response["data"] = handle.read()
        else:
          response["data"] = ""
        response["time"] = time.time() - inicio

    logger.info("Terminado en %.2f segundos" % (response["time"]))
    logger.info("Response sucess: %s" % (response["sucess"]))
    logger.info("Response code: %s" % (response["code"]))
    logger.info("Response error: %s" % (response["error"]))
    logger.info("Response data length: %s" % (len(response["data"])))
    logger.info("Response headers:")
    for header in response["headers"]:
        logger.info("- %s: %s" % (header, response["headers"][header]))

    if cookies:
        cookies_lock.acquire()
        logger.info("Guardando cookies...")
        cj.save(ficherocookies, ignore_discard=True)
        cookies_lock.release()

    logger.info("Encoding: %s" % (response["headers"].get('content-encoding')))

    if response["headers"].get('content-encoding') == 'gzip':
        logger.info("Descomprimiendo...")
        try:
            response["data"] = gzip.GzipFile(fileobj=StringIO(response["data"])).read()
            logger.info("Descomprimido")
        except:
            logger.info("No se ha podido descomprimir")

    # Anti cloudfare
    if "cf-ray" in response["headers"] and "refresh" in response["headers"]:
        wait_time = int(response["headers"]["refresh"][:1])
        auth_url = "%s://%s/%s" % (urlparse.urlparse(url)[0], urlparse.urlparse(url)[1],
                                   response["headers"]["refresh"][7:])

        logger.info("cloudflare detectado, esperando %s segundos..." % wait_time)
        time.sleep(wait_time)
        logger.info("Autorizando... url: %s" % auth_url)
        if downloadpage(auth_url, headers=headers, replace_headers=replace_headers).sucess:
            logger.info("Autorización correcta, descargando página")
            resp = downloadpage(url=url, post=post, headers=headers, timeout=timeout, follow_redirects=follow_redirects,
                                cookies=cookies, replace_headers=replace_headers, add_referer=add_referer)
            response["sucess"] = resp.sucess
            response["code"] = resp.code
            response["error"] = resp.error
            response["headers"] = resp.headers
            response["data"] = resp.data
            response["time"] = resp.time
        else:
            logger.info("No se ha podido autorizar")

    return type('HTTPResponse', (), response)


class NoRedirectHandler(urllib2.HTTPRedirectHandler):

    def http_error_302(self, req, fp, code, msg, headers):
        infourl = urllib.addinfourl(fp, headers, req.get_full_url())
        infourl.status = code
        infourl.code = code
        return infourl

    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302
