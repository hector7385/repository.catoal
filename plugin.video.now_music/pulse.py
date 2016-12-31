# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: Pulse
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.now_music'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "PL_34_m4eTlaMSONcN_P4r5QFAWAwkngbX"
YOUTUBE_CHANNEL_ID_2 = "PL_34_m4eTlaOeNd6fP9MspKqh9ksDiNtm"
YOUTUBE_CHANNEL_ID_3 = "PLLK5DjpAskR68KFNnVgvq5mZHEXTQIyX7"
YOUTUBE_CHANNEL_ID_4 = "PL_34_m4eTlaOFcXryY7OFbYGtK5Y1JoIa"
YOUTUBE_CHANNEL_ID_5 = "PL_34_m4eTlaOtJMirQzXvOoAwdechWbhF"
YOUTUBE_CHANNEL_ID_6 = "PL_34_m4eTlaMf-42RHro2x2UVMHNEkLvD"
YOUTUBE_CHANNEL_ID_7 = "PL_34_m4eTlaN5Dj1kIzrJMX95HRBLqeQr"
YOUTUBE_CHANNEL_ID_8 = "PL1659BED42584319F"
YOUTUBE_CHANNEL_ID_9 = "PL8FA9A7569EBB5E4A"
YOUTUBE_CHANNEL_ID_10 = "PL_34_m4eTlaPzdgA9RG_BlIImsUwCVkzy"
YOUTUBE_CHANNEL_ID_11 = "PL_34_m4eTlaNHt6GM5dOnraJ2zdE4R2Z_"
YOUTUBE_CHANNEL_ID_12 = "PLO47Lo58fyaJTRmPSH3eIx4R92WngXEeu"
YOUTUBE_CHANNEL_ID_13 = "PLBB7D0AF873F8FAEA" 
YOUTUBE_CHANNEL_ID_14 = "PL912C2772F94A73F9" 
YOUTUBE_CHANNEL_ID_15 = "PL_IGfDhmSGBMtrZrP0X440vgv5iBRfhy4"
YOUTUBE_CHANNEL_ID_16 = "PL6CDBDD2A3C0D55A5"
YOUTUBE_CHANNEL_ID_17 = "PLziBTZqySBRFOFOwbSuPn4GtockoGot7k" 
YOUTUBE_CHANNEL_ID_18 = "PLDouWbMQEftHiTge92lMQFgbNVUCBlP8E"
YOUTUBE_CHANNEL_ID_19 = "PLDouWbMQEftFRzud9bJO0Yg03R6TaJoL3"
YOUTUBE_CHANNEL_ID_20 = "PLDouWbMQEftHqrKjdu7cFSACIudT2n5Il" 
YOUTUBE_CHANNEL_ID_21 = "PL_34_m4eTlaNLsqqXEC3D-QPlMpgGqrFy"
YOUTUBE_CHANNEL_ID_22 = "PL6A8E66F870D64825"
YOUTUBE_CHANNEL_ID_23 = "PL_34_m4eTlaMDLrSesIGNfArzdqbV9PtO" 
YOUTUBE_CHANNEL_ID_24 = "PL_34_m4eTlaOcF4HOTM5_u7WEz5UOknPc"
YOUTUBE_CHANNEL_ID_25 = "PL_34_m4eTlaP6n2tYDBKamuvoQDo89a97"
YOUTUBE_CHANNEL_ID_26 = "PL_34_m4eTlaOoOkgbOgS93OFQ9QxTPJYP"
YOUTUBE_CHANNEL_ID_27 = "PL_34_m4eTlaMBcJhd_fEj-QBpb8P89F28" 
YOUTUBE_CHANNEL_ID_28 = "PL_34_m4eTlaN1pIJXJpatZyWCnQgPr_nU"
YOUTUBE_CHANNEL_ID_29 = "PL_34_m4eTlaOh7AX4GJRnnxKgJ5n9_V-M"
YOUTUBE_CHANNEL_ID_30 = "PL_34_m4eTlaMnTgbpMYRKfReUqZw1LRuJ"
YOUTUBE_CHANNEL_ID_31 = "PLuDr0us3k-BveJdm67f8SlDt87aRtyZ2r"
YOUTUBE_CHANNEL_ID_32 = "PL_34_m4eTlaMMi2E-nHwk4OdRi3OJQ78b"
YOUTUBE_CHANNEL_ID_33 = "PL_34_m4eTlaMO4Mz_dWge1XC9K2uhXThR" 
YOUTUBE_CHANNEL_ID_34 = "PL_34_m4eTlaPl5bRHTsf1kogkcS80LiEi"
YOUTUBE_CHANNEL_ID_35 = "PL1F0D80E99F7850E5"
YOUTUBE_CHANNEL_ID_36 = "PL_34_m4eTlaOryUpz8B44gf1tyxsyEJL1"
YOUTUBE_CHANNEL_ID_37 = "PLDouWbMQEftGj0O3468TrleWCTMTJrS20"
YOUTUBE_CHANNEL_ID_38 = "PLDouWbMQEftGzuFV8LqaBidN4Nr3WGWLk" 
YOUTUBE_CHANNEL_ID_39 = "PL_34_m4eTlaPcjuqnypKfhVVpHKmT4yxH"
YOUTUBE_CHANNEL_ID_40 = "PL_34_m4eTlaOg18XvgjqGTvFtX26QqIui"
YOUTUBE_CHANNEL_ID_41 = "PL_34_m4eTlaOakp50tDGnTQ2fwt4U8ewy"
YOUTUBE_CHANNEL_ID_42 = "PL_34_m4eTlaM_-9ciPXJA33ncF322YWA5"
YOUTUBE_CHANNEL_ID_43 = "PL_34_m4eTlaPSdTUlEYBLM4ewrck1RDvh" 
YOUTUBE_CHANNEL_ID_44 = "PLwNBYqY3GP2f9DZr6XdDgW8VwyPEX9bm7"
YOUTUBE_CHANNEL_ID_45 = "PLMw8cPF2uPc6eneUtoFamsrvGGZlF2uqL"
YOUTUBE_CHANNEL_ID_46 = "PLDouWbMQEftEHpZkhMpIwlWz1iE96HbQq"
YOUTUBE_CHANNEL_ID_47 = "PLDouWbMQEftFtfaMjEM-9IjipNjw7qJ5W"
YOUTUBE_CHANNEL_ID_48 = "PLDouWbMQEftH195uyZ0SlBVSznM61I8J3" 
YOUTUBE_CHANNEL_ID_49 = "PLDouWbMQEftHe0rKzAJPb7MGltCPtFxNs"
YOUTUBE_CHANNEL_ID_50 = "PLgK4BjZPsT825ISNA4dWqsnUuUQEfHZEu"
YOUTUBE_CHANNEL_ID_51 = "PLDouWbMQEftHJSvaRvBzvFZ4S34kucnwl"
YOUTUBE_CHANNEL_ID_52 = "PLDouWbMQEftF5HyM_lheKxX38sRZdcdfR"
YOUTUBE_CHANNEL_ID_53 = "PLDouWbMQEftEasB5KoU8faJqOQVCOq810" 
YOUTUBE_CHANNEL_ID_54 = "PLDouWbMQEftEcdNjhvM5YeVvXSl9nxOaU"
YOUTUBE_CHANNEL_ID_55 = "PL8Mowahw6-au9odO_rwNnWcxgdTdNVr_3"
YOUTUBE_CHANNEL_ID_56 = "PLDouWbMQEftF-RQMo2YsYzrR_ZByg947D"
YOUTUBE_CHANNEL_ID_57 = "PLDouWbMQEftEcdNjhvM5YeVvXSl9nxOaU"
YOUTUBE_CHANNEL_ID_58 = "PLDouWbMQEftEDrxxz3VoXIEfiQbYeOJ2l" 
YOUTUBE_CHANNEL_ID_59 = "PLDouWbMQEftEAJUcUYopDaqCbcmMIlIMl"
YOUTUBE_CHANNEL_ID_60 = "PLDouWbMQEftHqvpVkKeBiPszLECporRWe"
YOUTUBE_CHANNEL_ID_61 = "PLDouWbMQEftEvDn_oWxYCOOcbLk86TJTV"
YOUTUBE_CHANNEL_ID_62 = "PLDouWbMQEftGij9_IK8pIwRZ9wf0rcYc9"
YOUTUBE_CHANNEL_ID_63 = "PLDouWbMQEftFRdgKkRkFOvCi69YxICjzI" 
YOUTUBE_CHANNEL_ID_64 = "PLDouWbMQEftEEeKB6GcLaDQbypvob4e10"
YOUTUBE_CHANNEL_ID_65 = "PLDouWbMQEftHfSufbFaP1N5UvSZwuBQxj"
YOUTUBE_CHANNEL_ID_66 = "PLDouWbMQEftEXRa9q30waTahj7mpRrttU"
YOUTUBE_CHANNEL_ID_67 = "PLDouWbMQEftEylNuZbUaDdnjEVb4K8NXk"
YOUTUBE_CHANNEL_ID_68 = "PLDouWbMQEftFPAozxK35cermZl8JmEm6w" 
YOUTUBE_CHANNEL_ID_69 = "PLDouWbMQEftH05DjkYFT35ubDtJ9-EDAQ"
YOUTUBE_CHANNEL_ID_70 = "PLDouWbMQEftFLmCbJNnxBqo925x89tJci"
YOUTUBE_CHANNEL_ID_71 = "PLDouWbMQEftE3cvxvmmZbmb5LHFSqquC2"
YOUTUBE_CHANNEL_ID_72 = "PLDouWbMQEftHVApkssY45f20pBKQkubda"
YOUTUBE_CHANNEL_ID_73 = "PLDouWbMQEftE3qNQFpHbwtds_fClgrosx" 
YOUTUBE_CHANNEL_ID_74 = "PLDouWbMQEftHbsC27ysUWGw4OxnKwgmSI"
YOUTUBE_CHANNEL_ID_75 = "PLDouWbMQEftGxi1_JHCEMj0Mg6xu8ofTS"
YOUTUBE_CHANNEL_ID_76 = "PLDouWbMQEftGppOc9H3k4OblZt7AkFJIe"
YOUTUBE_CHANNEL_ID_77 = "PLDouWbMQEftFwkKFJg_dqrNZmViR_5Vpw"
YOUTUBE_CHANNEL_ID_78 = "PLDouWbMQEftGm-SYQFcZgSkl5Xsoi6ec3" 
YOUTUBE_CHANNEL_ID_79 = "PLDouWbMQEftG7H9iL5_e-05Qln6eOHzhJ"
YOUTUBE_CHANNEL_ID_80 = "PLDouWbMQEftFo66cP_Slk1oCoVZRVPQae"
YOUTUBE_CHANNEL_ID_81 = "PLDouWbMQEftGIy9zgfcIK_T0Qt0J_VJ5C"
YOUTUBE_CHANNEL_ID_82 = "PLDouWbMQEftHsFyHSBua-RZLFsx--Cu4U"
YOUTUBE_CHANNEL_ID_83 = "PLDouWbMQEftFfvSiP-qJnSRplBPtP9V0b" 
YOUTUBE_CHANNEL_ID_84 = "PLDouWbMQEftFtXgRrax8PJPPC1gdQIJ70"
YOUTUBE_CHANNEL_ID_85 = "PLDouWbMQEftGVhou1WEt7puGQOB7Ieiqw"
YOUTUBE_CHANNEL_ID_86 = "PLDouWbMQEftGnfnnc1hgtKo47JFFZO43A"
YOUTUBE_CHANNEL_ID_87 = "PLDouWbMQEftFoFXgF3j3d-2ViUyC8KXxV" 
YOUTUBE_CHANNEL_ID_88 = "PLDouWbMQEftEpPsQuisDX830NEqIg6pLB"
YOUTUBE_CHANNEL_ID_89 = "PLDouWbMQEftE9awijXpVSoSbRho30vX8Z"
YOUTUBE_CHANNEL_ID_90 = "PL1CAE497B646AD1A6"
YOUTUBE_CHANNEL_ID_91 = "PL729690CF3DC4038B"
YOUTUBE_CHANNEL_ID_92 = "PL91AE51E5AD495C42" 
YOUTUBE_CHANNEL_ID_93 = "PL395E7954B52B4822"
YOUTUBE_CHANNEL_ID_94 = "PLoDgQlTbBQzbdvhDlUw9NY4IW-RgpZ62E"
YOUTUBE_CHANNEL_ID_95 = "PL_34_m4eTlaP1Oisln8FWSQ-uJfb-jJfO"
YOUTUBE_CHANNEL_ID_96 = "PL_34_m4eTlaN0b1Wntb0io2m_j0Bbe1Id" 
YOUTUBE_CHANNEL_ID_97 = "PLFHCz0ifDWM1F-kNF9Kpo_WMniLJSDJYG"
YOUTUBE_CHANNEL_ID_98 = "PL_34_m4eTlaNQBMQYxfxQLN7eUkIKP66y"
YOUTUBE_CHANNEL_ID_99 = "PLQa1P8Aw9Jz9u3H6qDnSMz91HFK05u8Qi" 
YOUTUBE_CHANNEL_ID_100 = "PLCyMOjFkWxz0x7YHwWgdkqCB4BZSOYlVu"
YOUTUBE_CHANNEL_ID_101 = "PL_34_m4eTlaNLWS-34FVBlr8ZnlTUFkiV"
YOUTUBE_CHANNEL_ID_102 = "PL_34_m4eTlaMs7Q4Imtz199e2K4agqwyP"
YOUTUBE_CHANNEL_ID_103 = "PL_34_m4eTlaNh63gxFpUwwAROXj5V3AX8" 
YOUTUBE_CHANNEL_ID_104 = "PL_34_m4eTlaMFVmKb3lBxVKMWkGXUKG9g"
YOUTUBE_CHANNEL_ID_105 = "PL_34_m4eTlaPXh3wyeVKGJJvjJtZ-kJXY"
YOUTUBE_CHANNEL_ID_106 = "PLf8Oo47thU_O5ZvVPjAymfbAHZt3Tgr9m"
YOUTUBE_CHANNEL_ID_107 = "PLUSRfoOcUe4aJ_afJI6Iw_d-IMx16iwnH"
YOUTUBE_CHANNEL_ID_108 = "PLUSRfoOcUe4YctgFFjWQqhbndPAX0eJ8c" 
YOUTUBE_CHANNEL_ID_109 = "PLCJyoxQW5ieKzjL8MH3qyvR1Kf6jT2_Rn"
YOUTUBE_CHANNEL_ID_110 = "PLF73D80737572C687"
YOUTUBE_CHANNEL_ID_111 = "PL_34_m4eTlaNZnmJKJqLfslC2oW3kNKWK"
YOUTUBE_CHANNEL_ID_112 = "PLft313ngIElbbRJBRLtnP59MUOuo24kGr"
YOUTUBE_CHANNEL_ID_113 = "PLHHnmhLfwSsaZzrbBUH_N0WB6cZFFeJ41" 
YOUTUBE_CHANNEL_ID_114 = "PL_34_m4eTlaP5cyIG-2hUcqF2bZxHgZlZ"
YOUTUBE_CHANNEL_ID_115 = "PL_34_m4eTlaMgClOUihGU5EKM0md93FCN"
YOUTUBE_CHANNEL_ID_116 = "PL_34_m4eTlaOrcFRHD9mG4zUilcXQS8uB"
YOUTUBE_CHANNEL_ID_117 = "PLsdPA0A_fKLmuHNuafb76kecjHqeGoBLs"
YOUTUBE_CHANNEL_ID_118 = "PLF0A9B9128F4397BD" 
YOUTUBE_CHANNEL_ID_119 = "PL_34_m4eTlaPLkaa4gLSJsWm86Z0H8i_U"
YOUTUBE_CHANNEL_ID_120 = "PL_34_m4eTlaO64lWBQeC7xfmlA9uKvS4G"
YOUTUBE_CHANNEL_ID_121 = "PLXAN7tYrZq7drpFeMFFn7CNzkF-FUVIBh"
YOUTUBE_CHANNEL_ID_122 = "PLUSRfoOcUe4ZHOPA0YgBcbwAVkJQ52HH_"
YOUTUBE_CHANNEL_ID_123 = "PLBBC3BAC472A1020F" 
YOUTUBE_CHANNEL_ID_124 = "PLnknRVaLM8J_02U2zaSzX_9wvfmctT1Xe"
YOUTUBE_CHANNEL_ID_125 = "PLEE1730DB6C1BDCB4"
YOUTUBE_CHANNEL_ID_126 = "PL_34_m4eTlaO8Wj-65W7BioLh50i_4Mzs"
YOUTUBE_CHANNEL_ID_127 = "PL_34_m4eTlaMA1WFX92nvR5NK1Z4dc42M"
YOUTUBE_CHANNEL_ID_128 = "PLfXJnC0pregyWgUZzmnzasnwxhCZw0uqK" 
YOUTUBE_CHANNEL_ID_129 = "PLflvWSBDC77jVrR_6MzUHBsITaIxn4jZ8"
YOUTUBE_CHANNEL_ID_130 = "PLKfO_IEZedrhfX21ih0rSRzLKPMFnsPcx"
YOUTUBE_CHANNEL_ID_131 = "PLC9uHuoWKsDwFs_bLjU1Xf9kK032tIukr"
YOUTUBE_CHANNEL_ID_132 = "PLsdPA0A_fKLlogBKy9a0UsGUngUm2Nu7O"
YOUTUBE_CHANNEL_ID_133 = "PL_34_m4eTlaMExaWbVfv24i5O5Q5ZBZXU"
YOUTUBE_CHANNEL_ID_134 = "PL_34_m4eTlaNf6TSaM9IfLd13R1lKaoYd"
YOUTUBE_CHANNEL_ID_135 = "PL_34_m4eTlaMYv6z-uHidbtQ199xd1EK1"
YOUTUBE_CHANNEL_ID_136 = "PL_34_m4eTlaPnat1HtGrigGFXywxRscUK"
YOUTUBE_CHANNEL_ID_137 = "PL_34_m4eTlaMnlJjHHCOyEK0jDM7_dHQ5"
YOUTUBE_CHANNEL_ID_138 = "PL-PXKb5jSjwZT2QzeJCIlYSqs0cZvy808"
YOUTUBE_CHANNEL_ID_139 = "UCfJPtULqanZ3K7trqtupvtQ"
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
        title="Now Karaoke Ed.España",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="http://i.imgur.com/1Jieu64.png",
        folder=True )
		
	
    plugintools.add_item( 
        #action="", 
        title="Now Los Exitos Del Año 2016",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="http://www.fonodisco.es/227689-thickbox_default/now-2016-varios-2-cds-cd-.jpg",
        folder=True )
	

    plugintools.add_item( 
        #action="", 
        title="Now 95",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="http://www.musicktorrent.com/images/articles/25/25282.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Now 94",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now-94-underwater2B2-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 93",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://www.officialcharts.com/media/650017/now-93-artwork.png?width=488.07157057654075&height=500",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 92",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/20150923101439/now92GROTTO_HR-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 91",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/20150611093502/now-91-CYMK-FINAL-HR-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 90",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/0/01/Now_90_UK_Cover.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 89",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-89-Final-Artwork-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 88",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/8/84/Now_88_UK_Cover.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 87",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now_87_EGG_final-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 86",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now86NEW_FINAL-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 85",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Pack-shot2-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 84",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/81087xfVSDL._SL1500_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 83",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://cdn.bigissue.com/sites/bigissue/files/now_thats_what_i_call_music_83.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 82",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://tshop.r10s.com/3dc/0b1/5e1c/4b6d/20d8/3df1/8455/112ce49d9a005056b75a2f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 81",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now-81.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 80",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://i47.tinypic.com/o360l.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 79",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW79_F_flop_CYMK-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 78",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/3/3b/Now78UK.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 77",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/N77snowboardYEL-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 76",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now76HR-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 75",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://www.covershut.com/covers/NOW-Thats-What-I-Call-Music!-75-2010-Front-Cover-37348.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 74",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now74Sflakes_final-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 73",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/N73_FINAL_HR-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 72",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-72-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 71",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-71-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 70",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-70-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 69",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-69-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 68",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61tRYeXQQCL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 67",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-67-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 66",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-66-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 65",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-65-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 64",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-64-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 63",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/a/ae/Now_63.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 62",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-62-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 61",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-61.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 60",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-60-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 59",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-59-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 58",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-58-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 57",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://photos.prnewswire.com/prnvar/20160105/319490",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 56",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/91QvXvWXU1L._SY355_.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 55",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/71kFlRrz8aL._SX355_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 54",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/5/52/Now_54.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 53",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/5/58/Now_53.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 52",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/c/c1/Now_52.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 51",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/1b/Now_51.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 50",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/b/b3/Now_50.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 49",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/11/Now_49.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 48",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/2/20/Now_48.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 47",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/81ynokvm4ML._SL1500_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 46",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/c/c0/Now_46.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 45",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/3/36/Now_45.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 44",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/6/60/Now_44.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 43",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/f/ff/Now_43.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 42",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/c/c7/Now_42.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 41",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/d/d6/Now_41.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 40",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/5/56/Now_40.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Now 39",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/e/e8/Now_39.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 38",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-38-1024x1024.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 37",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="http://cps-static.rovicorp.com/3/JPG_400/MI0002/367/MI0002367718.jpg?partner=allrovi.com",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 36",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/e/ef/Now_36.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 35",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-35-1024x1003.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 34",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/a/a6/Now_34.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 33",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/d/d6/Now_33.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 32",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Now_32.jpg/220px-Now_32.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 31",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/15/Now_31.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 30",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="http://cdn.hitfix.com/photos/71216/Now30Front_rz_img_featured_photo_gallery.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 29",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/f/f8/Now_That's_What_I_Call_Music!_29_US_album_cover.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 28",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="http://images.coveralia.com/audio/n/Now_28--Frontal.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 27",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/8/80/Now_That's_What_I_Call_Music!_27_(UK_series)_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 26",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/41cCLInJypL._SX355_.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 25",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/61TH%2BnVIC2L._SY300_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 24",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/7/7e/Now_24.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 23",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/4/40/Now_23.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 22",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="http://www.music-bazaar.com/album-images/vol1/96/96327/612368-big/Now-That-S-What-I-Call-Music-22-cover.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 21",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="http://www.yosmusic.com/wp-content/uploads/2016/02/Now-21-%D7%97%D7%93%D7%A9.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 20",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://www.room512.co.uk/images/now20.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 19",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/61AMZA9HKDL.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 18",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="http://mtv.walla.co.il/wp-content/uploads/2012/09/Now18_CYMK_FINAL1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 17",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="http://mtv.walla.co.il/wp-content/uploads/2011/09/NOW-17-500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 16",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="http://destinyxnowmusic.freehostia.com/nowmusic/nowisrael16.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 15",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="http://cps-static.rovicorp.com/3/JPG_400/MI0000/410/MI0000410973.jpg?partner=allrovi.com",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 14",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://destinyxnowmusic.freehostia.com/nowmusic/nowisrael14.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 13",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="https://agencyspace.files.wordpress.com/2013/01/13.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 12",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="http://streamd.hitparade.ch/cdimages/-now_thats_what_i_call_music_12_[us]_a.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 11",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="http://media.israel-music.com/images/27932721.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 10",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61U1rUpKC2L.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 9",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/14/Now_9_United_Kingdom.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 8",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/a/aa/Now_8_United_Kingdom.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 7",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="http://rymimg.com/lk/f/l/c33af130e24ba021d2b963fa81008e24/2391455.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 6",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/818bzGDAdjL._SY355_.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 5",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/1b/Now_5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 4",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/2/24/Now_4_US.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now 3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="http://rymimg.com/lk/f/l/a4689d7fd545e470064441b21667fd92/2384145.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="http://streamd.hitparade.ch/cdimages/-now_thats_what_i_call_music_2_a_1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 1",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="http://lifestoogood.net/wp-content/uploads/2011/10/Now-1-300x300.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now Christmas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_134+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/20150814114319/Christmas_Hi_Res-1024x901.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now DriveTime",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-DRIVE-1500X1500-1024x1024.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now Dance Hits",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-DANCE-COVER--150x150.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Now Fitness ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="http://store.hmv.com/HMVStore/media/product/289482/01-289482.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Now Brit Hits",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/brits-png-1024x1024.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Party Anthems",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/imageFull/.faYg-MDV/ArticleSharedImage-57508.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Classic Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/61IeOgC6FyL._SY300_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Pop",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/imageFull/.fgn3yf9U/ArticleSharedImage-54831.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Disco",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/image250/.fWMTnFAU/ArticleSharedImage-11838.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Feel Good",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/image250/.fmiWtSSU/ArticleSharedImage-11581.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Running",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="http://tesco.scene7.com/is/image/tesco/521-8951_PI_1000025MN?id=6eebz3&fmt=jpg&fit=constrain,1&wid=250&hei=250",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Song",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61wQSnctNeL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Singer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/imageFull/.fA02I1_U/ArticleSharedImage-55818.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now House",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/image250/.fsmQrW6U/ArticleSharedImage-53676.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Summer Party",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="http://direct-ns.rhap.com/imageserver/v2/albums/Alb.189415979/images/500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Summer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/image250/.fPZ57mZU/ArticleSharedImage-23242.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Drive",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="https://images-eu.ssl-images-amazon.com/images/I/61EoE0udUkL._SL500_AA280_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/image250/.f6RaLMHU/ArticleSharedImage-33701.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Disney",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/819lN7C5loL._SL1500_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Reggae",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_110+"/",
        thumbnail="https://i.scdn.co/image/424aa797636f9477e07b1d168498c7c75c53a566",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",
        thumbnail="http://loudwire.com/files/2016/01/unnamed-10.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Country",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Nowcountryfeat.jpg/220px-Nowcountryfeat.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Legends",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",
        thumbnail="https://artwork-cdn.7static.com/static/img/sleeveart/00/039/687/0003968720_500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Power Ballads",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",
        thumbnail="http://img15.nnm.me/e/7/5/1/1/8b4a5c0dd668f2997a8e09f1695_prev.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 80's",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/817iO3O9vfL._SL1500_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 90's",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_116+"/",
        thumbnail="http://tesco.scene7.com/is/image/tesco/493-2421_PI_1000025MN?wid=493&ht=538",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 00's",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/now00s.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now No.1's",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOWno1s.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 21st Century",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",
        thumbnail="http://dhgkpqsiufwl2.cloudfront.net/media/ArticleSharedImage/image250/.f7e16dUU/ArticleSharedImage-28286.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Sing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",
        thumbnail="http://midlifegamer.net/wp-content/uploads/2015/10/NTWICS.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Party",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/Now-Party-1024x1024.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Now Rock Ballads",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/618hAw24%2BRL._SY300_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Chilled",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",
        thumbnail="https://images-eu.ssl-images-amazon.com/images/I/61Q9IGKQZBL._SL500_AA280_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Musicals",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOWMusicals2.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now USA",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/81nq7JhBUUL._SL1417_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 25 Years",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-25-Years.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now 30 Years",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",
        thumbnail="http://thelatest.co.uk/files/2013/05/Now-30-Years-Sleeve.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now R&B",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/nowrb.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Million",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",
        thumbnail="http://www.officialcharts.com/media/318845/now_thats_what_i_call_a_million.jpg?width=500&height=500",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Club Hits",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_127+"/",
        thumbnail="http://cdn.smehost.net/nowmusiccom-ukprod/wp-content/uploads/NOW-Club-Hits-1024x900.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Love",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/e/e2/Now_That's_What_I_Call_Love_3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Now Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",
        thumbnail="http://a1491.phobos.apple.com/us/r30/Purple4/v4/c2/b7/97/c2b79704-18bf-960c-f5f6-877b12af4af1/mzl.vmknkzkm.png",
        folder=True )

run()