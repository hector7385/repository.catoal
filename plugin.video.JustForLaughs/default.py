# -*- coding: utf-8 -*-
#------------------------------------------------------------
#Catoal Kodi Addon
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.JustForLaughs'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCpsSadsgX_Qk9i6i_bJoUwQ"

# Entry point
def run():
    plugintools.log("docu.run")
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR lime]Bienvenidos A Just For Laughs[/COLOR] [COLOR blue]Ca[/COLOR][COLOR yellow]to[/COLOR][COLOR red]al[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://static.tumblr.com/pr2qxbx/ga3m4nd6r/logo_english.jpg",
		fanart="http://crookedpixels.com/wp-content/uploads/2013/07/just-for-laughs3.jpg",
        folder=True )

run()
