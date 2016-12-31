# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Canal para cineblog01
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os
import sys
import re, htmlentitydefs

from core import scrapertools
from core import logger
from core import config
from platformcode import platformtools
import xbmcplugin
import xbmcaddon
from core.item import Item
from core import servertools
import xbmc
import xbmcgui
import time


__channel__ = "arenavision"
__category__ = "F,S,A"
__type__ = "generic"
__title__ = "Arenavision"
__language__ = "ES"


host ="http://arenavision.in"
song = os.path.join(config.get_runtime_path(), 'music', 'best-day-of-my-life.mp3')
DEBUG = config.get_setting("debug")
def isGeneric():
    return True

def agendaglobal(item):
    itemlist = []
    try:
        item.url = "http://arenavision.in/schedule"
        item.thumbnail = "http://s6.postimg.org/as7g0t9qp/STREAMSPORTAGENDA.png"
        item.fanart = "http://s6.postimg.org/5utvfp7rl/streamsportonairfan.jpg"
        itemlist = mainlist(item)
        if itemlist[-1].action == "mainlist":
            itemlist.pop()
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []
    
    return itemlist


def mainlist(item):
    logger.info("pelisalacarta.arenavision schedule")
    
    itemlist = []
    import xbmc
    check=xbmc.getInfoLabel('ListItem.Title')
   
    if item.channel != __channel__:
        item.channel = __channel__
    else:
        xbmc.executebuiltin('xbmc.PlayMedia('+song+')')
    
    # Descarga la página
    item.url="http://arenavision.in/schedule"
    data = scrapertools.cache_page(item.url)
    data=re.sub(r"\n|\r|\t|\s{2}|&nbsp;|<br />","",data)
    patron_bloque = '</style><p></p><p></p>(.*?)Brusells'
    matchesenlaces = re.compile(patron_bloque,re.DOTALL).findall(data)
    
    for pepe in matchesenlaces:
        patron = 'auto-style3.*?>(\d+/\d+/\d+).*?auto-style3.*?>(.*?)CET.*?auto-style3.*?>(.*?)</td>.*?auto-style3.*?>(.*?)</td>.*?auto-style3.*?>(.*?)</td>.*?auto-style3.*?>(.*?)</td>'
        matches = re.compile(patron,re.DOTALL).findall(pepe)

        for dia , hora, deportes,competicion, partido, av_leng in matches:
            hora = hora.strip()
            av_leng = re.sub(r"<br />\n\t\t","--",av_leng)
            date=scrapertools.get_match(dia,'(\d+/\d+)/')
            time= hora
            evento = partido
            deporte = deportes
            if  "SOCCER" in deporte:
                 evento = evento.replace("-", " vs ")
                 deporte = "futbol"
            dia = "[COLOR darkkhaki][B]"+dia+"[/B][/COLOR]"
            hora = "[COLOR chartreuse][B]"+hora+"[/B][/COLOR]"
            deportes = "[COLOR burlywood][B]"+deportes+"[/B][/COLOR]"
            partido = "[COLOR orangered][B]"+partido+"[/B][/COLOR]"
            competicion = "[COLOR darkgoldenrod][B]"+competicion+"[/B][/COLOR]"
            espacio = "[COLOR floralwhite]--[/COLOR]"
            title = dia +espacio+hora+espacio+"[COLOR beige][B][[/B][/COLOR]"+ deportes +"[COLOR beige][B]][/B][/COLOR]"+espacio+partido +espacio+ "[COLOR gainsboro][B]([/B][/COLOR]"+competicion+"[COLOR gainsboro][B])[/B][/COLOR]"
            #title = re.sub(r"<br />","",title)
            itemlist.append( Item(channel=__channel__, title=title,action="enlaces",url = "",extra= av_leng , thumbnail= "http://s6.postimg.org/csumvetu9/arenavisionthumb.png",fanart="http://s6.postimg.org/e965djwr5/arenavisionfan.jpg",fulltitle= partido,date=date, time=time, evento=evento, deporte=deporte, context="info_partido", folder=False) )
    return itemlist

def enlaces(item):
    logger.info("pelisalacarta.arenavision scraper")
    itemlist = []
    import xbmcgui
    datos = item.extra
    ventana = TextBox1(datos=datos, item= item)
    ventana.doModal()

ACTION_PREVIOUS_MENU = 10
ACTION_SELECT_ITEM = 7
class TextBox1( xbmcgui.WindowDialog ):
        """ Create a skinned textbox window """
        def __init__( self, *args, **kwargs):
            self.datos = kwargs.get('datos')
            self.item =  kwargs.get('item')
            item = self.item
            xbmc.executebuiltin('Action(Select)')
        
        def onAction(self, action):
            if action == ACTION_PREVIOUS_MENU :
                self.close()
                
                
        
            elif action == ACTION_SELECT_ITEM  :
                if xbmc.Player().isPlayingVideo():
                   xbmc.log("pepezno")
                   self.close()
                
                else:
                   
                   check_skin =xbmc.getSkinDir()
                   self.show()
                   datos = self.datos
                   self.background = xbmcgui.ControlImage( -40, -40, 1500, 830, 'https://s6.postimg.org/dx5tgv5e9/arenavfondo.png')
                   self.addControl(self.background)
                   item = self.item
                   fulltitle = item.fulltitle
                   
                   select=Select('DialogSelect.xml',datos,fulltitle)
            
                   select.doModal()
                   if not "confluence" in check_skin:
                      if xbmc.Player().isPlayingVideo():
                         xbmc.sleep(550)
                         self.close()
                         xbmc.sleep(550)
                      else:
                         self.close()
                   if "confluence" in check_skin:
                       xbmc.sleep(550)
                       self.close()
                       xbmc.sleep(550)
                    

ACTION_GESTURE_SWIPE_LEFT = 511
ACTION_SELECT_ITEM = 7
ACTION_MOVE_RIGHT = 2
ACTION_MOVE_LEFT = 1
ACTION_PREVIOUS_MENU = 10
ACTION_MOUSE_LEFT_CLICK = 100
ACTION_MOUSE_RIGHT_CLICK = 101
OPTIONS_OK = 5
OPTION_PANEL = 6
class Select(xbmcgui.WindowXMLDialog):
       def __init__( self, item,datos,fulltitle ):
           
           self.datos = datos
           self.fulltitle = fulltitle

       def onInit(self):
           try:
              self.control_list = self.getControl(6)
              self.getControl(5).setNavigation(self.control_list, self.control_list, self.control_list, self.control_list)
              self.getControl(3).setEnabled(0)
              self.getControl(3).setVisible(0)
           except:
                pass
           self.getControl(1).setLabel("[COLOR orange][B]Selecciona Canal...[/B][/COLOR]")
           self.getControl(5).setLabel("[COLOR tomato][B]Cerrar[/B][/COLOR]")
           self.control_list.reset()
           items = []
           self.datos = re.sub(r" ","-",self.datos)
           patron = '(.*?)\[(.*?)\]'
           matches = re.compile(patron,re.DOTALL).findall(self.datos)
           
           if len(matches)==0 :
               av= "[COLOR crimson][B]Sin canal[/B][/COLOR]"
               thumbnail="http://s6.postimg.org/vq2l1wz2p/noacestreamsopcast.png"
               item = xbmcgui.ListItem(str(av))
               item.setArt({"thumb":str(thumbnail)})
               items.append(item)
           for canales, idioma in matches:
                matchescanales = canales[:-1].split("-")
                for av in matchescanales:
                    url ="http://arenavision.in/av"+av
                    if not "S" in av:
                       thumbnail ="https://s6.postimg.org/hq3soxkep/acestream.png"
                       title = "[COLOR crimson]AV[/COLOR]"+" "+"[COLOR floralwhite]"+av+"[/COLOR]"+ " "+"[COLOR palegreen]Idioma[/COLOR]"+" "+"[COLOR palegreen]"+idioma+"[/COLOR]"
                    else:
                       av = re.sub(r'S','',av)
                       thumbnail = "https://s6.postimg.org/734xme5xt/sopcast.png"
                       title = "[COLOR crimson]AV[/COLOR]"+" "+"[COLOR floralwhite]"+av+"[/COLOR]"+ " "+"[COLOR deepskyblue]Idioma[/COLOR]"+" "+"[COLOR deepskyblue]"+idioma+"[/COLOR]"
                    #av = av + "("+idioma+")"
                    self.url = url
                    item = xbmcgui.ListItem(str(title))
                    try:
                       item.setArt({"thumb":str(thumbnail)})
                    except:
                       item.setThumbnailImage(thumbnail)
                    item.setProperty("url",url)
                    items.append(item)
           self.getControl(6).addItems(items)
           self.setFocusId(6)

       def onAction(self,action):
           if action.getId() == ACTION_SELECT_ITEM and not controlId()== OPTIONS_OK:
               xbmc.executebuiltin('xbmc.PlayMedia(Stop)')
               self.list = self.getControl(6)
               selecitem=self.list.getSelectedItem()
               url = selecitem.getProperty("url")
               data = scrapertools.cache_page(url)
               url = servertools.findvideosbyserver(data, "p2p")
               if url:
                   url = url[0][1]
               #Creamos el item para platformtools
               item =Item()
               item.fulltitle = self.fulltitle
               item.url = url + "|" + item.fulltitle
               item.server = "p2p"
               self.close()
               check_skin =xbmc.getSkinDir()
               
               if not "confluence" in check_skin :
                   xbmc.sleep(300)
                   xbmc.executebuiltin('Action(PreviousMenu)')
                   xbmc.sleep(300)
               
               platformtools.play_video(item)
               self.close()
               check_skin =xbmc.getSkinDir()
               
               if "confluence" in check_skin :
                   if xbmc.Player().isPlayingVideo():
                       #xbmc.sleep(300)
                       xbmc.executebuiltin('Action(PreviousMenu)')
                   else:
                       xbmc.executebuiltin('Action(PreviousMenu)')
               else:
                    xbmc.executebuiltin('Action(PreviousMenu)')
           elif action.getId() == ACTION_PREVIOUS_MENU or action.getId()==ACTION_MOUSE_RIGHT_CLICK or action == 92:
               
                self.close()
                xbmc.sleep(300)
                xbmc.executebuiltin('Action(PreviousMenu)')

                
       def onClick(self,controlId):
           if controlId == OPTION_PANEL:
               xbmc.executebuiltin('xbmc.PlayMedia(Stop)')
               self.list = self.getControl(6)
               selecitem=self.list.getSelectedItem()
               url = selecitem.getProperty("url")
               data = scrapertools.cache_page(url)
               url = servertools.findvideosbyserver(data, "p2p")
               if url:
                   url = url[0][1]
               #Creamos el item para platformtools
               item =Item()
               item.fulltitle = self.fulltitle
               item.url = url + "|" + item.fulltitle
               item.server = "p2p"
               self.close()
               check_skin =xbmc.getSkinDir()
               
               if not "confluence" in check_skin :
                   xbmc.sleep(300)
                   xbmc.executebuiltin('Action(PreviousMenu)')
                   xbmc.sleep(300)
               
               
               platformtools.play_video(item)
               check_skin =xbmc.getSkinDir()
               
               if "confluence" in check_skin :
                   if xbmc.Player().isPlayingVideo():
                       #xbmc.sleep(300)
                       xbmc.executebuiltin('Action(PreviousMenu)')
                   else:
                      xbmc.executebuiltin('Action(PreviousMenu)')
               else:
                    xbmc.executebuiltin('Action(PreviousMenu)')
           
           elif controlId == OPTIONS_OK:
               self.close()
               TESTPYDESTFILE = xbmc.translatePath('special://skin/720p/DialogSelect2.xml')
               xbmc.sleep(300)
               xbmc.executebuiltin('Action(PreviousMenu)')

''' patron = '(AV\d+)'
    matches = re.compile(patron,re.DOTALL).findall(item.extra)
    for (i , f) in enumerate(matches):
        if "AV" in f:
            a = re.compile('AV(\d+)',re.DOTALL).findall(f)
            for (b,c) in enumerate(a):
                   
                   
                if c== "9" or c =="8" or c =="7" or c =="6" or c =="5" or c =="4" or c =="3" :
                    c= " "+c
                   
                if c <= "20" :
                    matches[i] = f.replace(f,"[COLOR crimson][B]"+matches[i]+"[/B][/COLOR]")+ "[COLOR palegreen][B]  Acestream[/B][/COLOR]"
                else:
                    matches[i] = f.replace(f,"[COLOR crimson][B]"+matches[i]+"[/B][/COLOR]")+ "[COLOR deepskyblue][B]  Sopcast[/B][/COLOR]"
            
            
        get_url= [(i,x) for i, x in enumerate(matches)]
        get_url = repr(get_url)
            #get_url= re.sub(r"\[COLOR.*?\]\[.*?]|\[.*?\]\[/COLOR\].*?\[.*?\]\[/COLOR\]","",get_url)
        print "marco"
        print get_url
        fulltitle =item.fulltitle
        print "pacopepe"
        print fulltitle
    index = xbmcgui.Dialog().select("[COLOR orange][B]Selecciona Canal...[/B][/COLOR]", matches)
        
    if index != -1:
        index =str(index)
        print "kkkk"
        print get_url
        if index == 0:
            catch_url=scrapertools.get_match(get_url,'\('+index+',.*?\'\[COLOR crimson\]\[B\](.*?)\[')
        catch_url=scrapertools.get_match(get_url,''+index+',.*?\'\[COLOR crimson\]\[B\](.*?)\[')
        url =urlparse.urljoin(host,catch_url)
            
        import xbmc
        xbmc.executebuiltin('xbmc.PlayMedia(Stop)')
        ### Esto sustituye a la función go
        data = scrapertools.cache_page(url)
        patron = '\*INFO.*?Click.*?<a href="([^"]+)"'
        url = scrapertools.find_single_match(data, patron)
        item.url = url +"|" + fulltitle
        print "tu vieja"
        print item.url
        item.server = "p2p"        
        platformtools.play_video(item)
			
    else:
        import xbmc
        xbmc.executebuiltin( "XBMC.Container.Update" )
        return


def press():
    import xbmc
    xbmc.executebuiltin('Action(Select)')'''
