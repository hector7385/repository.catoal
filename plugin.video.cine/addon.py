# -*- coding: utf-8 -*-
import sys,os,re,unicodedata
import xbmcgui
import xbmcplugin
import xbmcaddon
import urllib,urllib2
import urlparse
from urlparse import parse_qsl
import sqlite3,base64
try:
    import cinecrypt
except:
    try:
        import cinecrypt1 as cinecrypt
    except:
        try:
            import cinecrypt2 as cinecrypt
        except:
            import cinecrypt3 as cinecrypt

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def checkbas(bas):
    cinecrypt.checkbas(bas)

def inputtext():
    import xbmc
    keyboard = xbmc.Keyboard("")
    keyboard.doModal()
    tecleado = ''
    if (keyboard.isConfirmed()):
        tecleado = keyboard.getText()
    return tecleado

my_addon = xbmcaddon.Addon()
addonpath = xbmc.translatePath(my_addon.getAddonInfo('path').decode('utf-8'))
profile = xbmc.translatePath(my_addon.getAddonInfo('profile').decode('utf-8'))
iconpath = os.path.join(addonpath, "resources/media/")
base = '%s/thebas.tmp' %profile
brko = '%s/rkobas.tmp' %profile
if not os.path.exists(profile):
    try:
        os.makedirs(profile)
    except: pass
args = urlparse.parse_qs(sys.argv[2][1:])
_url = sys.argv[0]
_handle = int(sys.argv[1])

def get_categories():
    categories = []
    categories.append({'title':'Géneros',             'action':'genero', 'ico':'gen'})
    categories.append({'title':'Temas',               'action':'tema'  , 'ico':'tem'})
    categories.append({'title':'Años',                'action':'anno'  , 'ico':'ann'})
    categories.append({'title':'Grupos',              'action':'grupo' , 'ico':'gru'})
    categories.append({'title':'Buscar por título',   'action':'bustit', 'ico':'bus'})
    categories.append({'title':'Buscar por director', 'action':'busdir', 'ico':'bus'})
    categories.append({'title':'Buscar por actor',    'action':'busact', 'ico':'bus'})
    categories.append({'title':'Buscar por grupo',    'action':'busgru', 'ico':'bus'})
    categories.append({'title':'Ver peli recomendada','action':'pelrec', 'ico':'bus'})
    categories.append({'title':'Últimas 100 nuevas',  'action':'ultim',  'ico':'bus'})
    categories.append({'title':'Últimas 100 viejas',  'action':'ultim2', 'ico':'bus'})
    return categories

def list_categories():
    checkbas(base)
    categories = get_categories()
    listing = []
    for category in categories:
        icon = '%s/%s.png' %(iconpath,category['ico'])
        list_item = xbmcgui.ListItem(label=category['title'], iconImage=icon)
        url = '{0}?action={1}'.format(_url, category['action'])
        is_folder = True
        listing.append((url, list_item, is_folder))
    try:
        xbmcplugin.setContent(_handle,"files")
        xbmc.executebuiltin("Container.SetViewMode(500)")
    except: pass
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def getgenero(pid):
    genero = ''
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT genero FROM generos INNER JOIN pelgen ON generos.id = pelgen.idgen where pelgen.idpel=? ORDER BY pelgen.id", (pid,))
    rows = cur.fetchall()
    conn.close()
    if rows:
        gen = []
        for row in rows:
            gen.append(row[0])
        genero = ', '.join(gen)
    return genero

def dolist(rows=[],tipo2=False,zid=''):
    try:
        xbmcplugin.setContent(_handle,"movies")
        xbmc.executebuiltin("Container.SetViewMode(515)")
    except: pass

    # List = 502
    # Big List = 51
    # Thumbnails = 500
    # Poster Wrap = 501
    # Fanart = 508
    # Media info = 504
    # Media info 2 = 503
    # Media info 3 = 515

    listing = []
    for row in rows:
        pid = row[0]
        srv = row[1]
        usr = row[2]
        col = row[3]
        pel = row[4]
        hd  = row[5]
        nom = row[6]
        ann = row[8]
        sin = row[9]
        img = row[11] 
        drt = row[12]
        img1 = row[21]
        img2 = row[22]
        genero = getgenero(pid)
        tit=nom
        if img1==None:
            img1 = img
        else:
            img1 = 'https://image.tmdb.org/t/p/w500%s' %img1
        if img2==None:
            img2 = img
        else:
            img2 = 'https://image.tmdb.org/t/p/original%s' %img2
        if hd == 'S':
            nom = '[COLOR khaki]%s (HD)[/COLOR]' %nom
        if tipo2:
            nom = '[COLOR orange]%s[/COLOR] %s' %(ann,nom)
        list_item = xbmcgui.ListItem(label=nom, iconImage=img)
        list_item.setInfo('video', {'title': nom, 'year': ann, 'director': drt, 'plot': sin, 'genre': genero})
        list_item.setArt({'thumb': img, 'icon': img1, 'fanart': img2})
        list_item.setProperty('IsPlayable', 'true')
        srv = '%s%s' %(srv,zid)
        url = '{0}?action=play&server={1}&user={2}&cole={3}&peli={4}&id={5}&tit={6}'.format(_url, srv, usr, col, pel, pid, base64.urlsafe_b64encode(tit.encode('utf-8')))
        is_folder = False
        listing.append((url, list_item, is_folder))
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def list_genero():
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT generos.id, genero, Count(idpel) FROM generos INNER JOIN pelgen ON generos.id = pelgen.idgen GROUP BY generos.genero ORDER BY genero2")
    rows = cur.fetchall()
    conn.close()
    listing = []
    for row in rows:
        gid = row[0]
        gen = row[1]
        cnt = row[2]
        title = '[COLOR gold]%s[/COLOR] (%s)' %(gen,cnt)
        list_item = xbmcgui.ListItem(label=title, iconImage='')
        url = '{0}?action=genero2&idgen={1}'.format(_url, gid)
        is_folder = True
        listing.append((url, list_item, is_folder))
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def list_genero2(idgen):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelis INNER JOIN pelgen ON pelis.ID = pelgen.idpel WHERE pelgen.idgen=? ORDER BY pelis.grupo, pelis.hd, pelis.id;", (idgen,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows)

def list_tema():
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT temas.id, tema, Count(idpel) FROM temas INNER JOIN peltem ON temas.id = peltem.idtem GROUP BY temas.tema ORDER BY tema2")
    rows = cur.fetchall()
    conn.close()
    listing = []
    for row in rows:
        gid = row[0]
        gen = row[1]
        cnt = row[2]
        title = '[COLOR gold]%s[/COLOR] (%s)' %(gen,cnt)
        list_item = xbmcgui.ListItem(label=title, iconImage='')
        url = '{0}?action=tema2&idtem={1}'.format(_url, gid)
        is_folder = True
        listing.append((url, list_item, is_folder))
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def list_tema2(idtem):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelis INNER JOIN peltem ON pelis.ID = peltem.idpel WHERE peltem.idtem=? ORDER BY pelis.grupo, pelis.hd, pelis.id;", (idtem,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows)

def list_anno():
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("Select anno,count(id) from pelis group by anno order by anno")
    rows = cur.fetchall()
    conn.close()
    listing = []
    for row in rows:
        anno = row[0]
        cnt = row[1]
        title = '[COLOR gold]%s[/COLOR] (%s)' %(anno,cnt)
        list_item = xbmcgui.ListItem(label=title, iconImage='')
        url = '{0}?action=anno2&anno={1}'.format(_url, anno)
        is_folder = True
        listing.append((url, list_item, is_folder))
    try:
        xbmcplugin.setContent(_handle,"files")
        xbmc.executebuiltin("Container.SetViewMode(502)")
    except: pass
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def list_anno2(anno):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("Select * from pelis where anno = ? order by grupo, hd;", (anno,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows)

def list_grupo():
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT grupos.id, grupo, Count(idgru) FROM grupos INNER JOIN pelgru ON grupos.id = pelgru.idgru GROUP BY grupos.id having count(grupos.id)>1 ORDER BY grupo2")
    rows = cur.fetchall()
    conn.close()
    listing = []
    for row in rows:
        gid = row[0]
        gen = row[1]
        cnt = row[2]
        title = '[COLOR gold]%s[/COLOR] (%s)' %(gen,cnt)
        list_item = xbmcgui.ListItem(label=title, iconImage='')
        url = '{0}?action=grupo2&idgru={1}'.format(_url, gid)
        is_folder = True
        listing.append((url, list_item, is_folder))
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def busca_por_grupo():
    texto = inputtext()
    if texto:
        conn = sqlite3.connect(base)
        cur = conn.cursor()
        texto = elimina_tildes(unicode(texto.decode('utf-8'))).upper()
        texto = '%'+texto+'%'
        cur.execute("SELECT grupos.id, grupo, Count(idgru) FROM grupos INNER JOIN pelgru ON grupos.id = pelgru.idgru WHERE grupo2 like ? GROUP BY grupos.id having count(grupos.id)>1 ORDER BY grupo2", (texto,))
        rows = cur.fetchall()
        conn.close()
        listing = []
        for row in rows:
            gid = row[0]
            gen = row[1]
            cnt = row[2]
            title = '[COLOR gold]%s[/COLOR] (%s)' %(gen,cnt)
            list_item = xbmcgui.ListItem(label=title, iconImage='')
            url = '{0}?action=grupo2&idgru={1}'.format(_url, gid)
            is_folder = True
            listing.append((url, list_item, is_folder))
        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)

def list_grupo2(idgru):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelis INNER JOIN pelgru ON pelis.ID = pelgru.idpel WHERE pelgru.idgru=? ORDER BY pelis.anno, pelis.grupo, pelis.hd, pelis.id;", (idgru,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows,True)

def busca_por_titulo():
    texto = inputtext()
    if texto:
        conn = sqlite3.connect(base)
        cur = conn.cursor()
        texto = elimina_tildes(unicode(texto.decode('utf-8'))).upper()
        texto = '%'+texto+'%'
        cur.execute("Select * from pelis where grupo like ? order by grupo", (texto,))
        rows = cur.fetchall()
        conn.close()
        dolist(rows)

def busca_por_director():
    texto = inputtext()
    if texto:
        conn = sqlite3.connect(base)
        cur = conn.cursor()
        texto = elimina_tildes(unicode(texto.decode('utf-8'))).upper()
        texto = '%'+texto+'%'
        cur.execute("Select director, count(id) from pelis group by director having director2 like ? order by director2", (texto,))
        rows = cur.fetchall()
        conn.close()
        listing = []
        for row in rows:
            drt = row[0].encode('utf-8')
            cnt = row[1]
            title = '[COLOR gold]%s[/COLOR] (%s)' %(drt,cnt)
            list_item = xbmcgui.ListItem(label=title, iconImage='')
            url = '{0}?action=busdir2&director={1}'.format(_url, drt)
            is_folder = True
            listing.append((url, list_item, is_folder))
        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)

def busca_por_director2(director):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("Select * from pelis where director = ? order by anno, grupo, id", (director.decode('utf-8'),))
    rows = cur.fetchall()
    conn.close()
    dolist(rows,True)

def busca_por_actor():
    texto = inputtext()
    if texto:
        conn = sqlite3.connect(base)
        cur = conn.cursor()
        texto = elimina_tildes(unicode(texto.decode('utf-8'))).upper()
        texto = '%'+texto+'%'
        cur.execute("SELECT actores.id, actor, Count(idact) FROM actores INNER JOIN pelact ON actores.id = pelact.idact GROUP BY actores.actor having actor2 like ? ORDER BY actor2", (texto,))
        rows = cur.fetchall()
        conn.close()
        listing = []
        for row in rows:
            aid = row[0]
            act = row[1]
            cnt = row[2]
            title = '[COLOR gold]%s[/COLOR] (%s)' %(act,cnt)
            list_item = xbmcgui.ListItem(label=title, iconImage='')
            url = '{0}?action=busact2&idact={1}'.format(_url, aid)
            is_folder = True
            listing.append((url, list_item, is_folder))
        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)

def busca_por_actor2(idact):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelis INNER JOIN pelact ON pelis.ID = pelact.idpel WHERE pelact.idact=? ORDER BY pelis.anno, pelis.grupo, pelis.id;", (idact,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows,True)

def ultimas():
    import datetime
    anno = datetime.datetime.now().year
    conn = sqlite3.connect(base)
    cur = conn.cursor()
   #cur.execute("SELECT * FROM pelis where anno>=? order by id DESC, hd LIMIT(100);", (anno-1,))
    cur.execute("SELECT * FROM pelis where gb is not null and anno>=? order by gb, HD LIMIT(100);", (anno-1,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows,False)

def ultimas2():
    import datetime
    anno = datetime.datetime.now().year
    conn = sqlite3.connect(base)
    cur = conn.cursor()
   #cur.execute("SELECT * FROM pelis where anno<? order by id DESC, hd LIMIT(100);", (anno-1,))
    cur.execute("SELECT * FROM pelis where gb is not null and anno<? order by gb, HD LIMIT(100);", (anno-1,))
    rows = cur.fetchall()
    conn.close()
    dolist(rows,False)

def peli_recomendada():
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute("Select id,genero from generos order by genero2;")
    rows = cur.fetchall()
    conn.close()
    listing = []
    title = '[COLOR gold]Selecciona un género[/COLOR]'
    list_item = xbmcgui.ListItem(label=title, iconImage='')
    is_folder = False
    listing.append(('', list_item, is_folder))
    for row in rows:
        gid = row[0]
        gen = row[1]
        list_item = xbmcgui.ListItem(label=gen, iconImage='')
        url = '{0}?action=pelrec2&idgen={1}'.format(_url, gid)
        is_folder = True
        listing.append((url, list_item, is_folder))
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def lista_random(idgen):
    connrk = sqlite3.connect(brko)
    currk = connrk.cursor()
    currk.execute('CREATE TABLE IF NOT EXISTS "vtas" (`id` INTEGER NOT NULL, `faffid` INTEGER NOT NULL, PRIMARY KEY(`id`));')

    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS "reko" (`id` INTEGER NOT NULL, `idpel` INTEGER NOT NULL, PRIMARY KEY(`id`));')
    cur.execute('delete from reko;')
    conn.commit()
    cur.execute("SELECT pelis.id,faffid,grupo FROM pelis INNER JOIN pelgen ON pelis.ID = pelgen.idpel WHERE pelis.valoracion>6.5 and pelgen.idgen=? ORDER BY pelis.id;", (idgen,))
    rows = cur.fetchall()
    lista=[]
    ya = []
    lng = len(rows)-1
    from random import randint
    while 1==1:
        num = randint(0,lng)
        if num not in ya:
            ya.append(num)
            row = rows[num]
            faffid = row[1]
            currk.execute("SELECT id from vtas where faffid=?;", (faffid,))
            rwrk = currk.fetchone()
            if not rwrk:
                currk.execute("INSERT INTO vtas(faffid) VALUES (?);", (faffid,))
                connrk.commit()
                item={}
                item['grupo'] = row[2]
                item['id'] = row[0]
                lista.append(item)
                if len(lista)==10:
                    break
            if len(ya)>lng:
                currk.execute("DELETE FROM vtas;")
                connrk.commit()
                break
    connrk.close()
    lista.sort(key=lambda x: x['grupo'])
    rids=[]
    for item in lista:
        cur.execute('INSERT INTO reko(idpel) VALUES (?);', (item['id'],))
        rids.append(str(item['id']))
    rids = '_%s' %'.'.join(rids)
    cur.execute("SELECT * FROM pelis INNER JOIN reko ON pelis.ID = reko.idpel ORDER BY reko.id;")
    rows = cur.fetchall()
    cur.execute('delete from reko;')
    conn.commit()
    conn.close()
    dolist(rows,False,rids)

def peli_recomendada2(idgen):
    conn = sqlite3.connect(base)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS "reco" (`id` INTEGER NOT NULL, `idpel` INTEGER NOT NULL, PRIMARY KEY(`id`));')
    conn.commit()
    cur.execute('select idpel from reco order by id;')
    rows = cur.fetchall()
    conn.close()
    if rows:
        zid = []
        for row in rows:
            zid.append(str(row[0]))
        zid = '_%s' %'.'.join(zid)
        conn = sqlite3.connect(base)
        cur = conn.cursor()
        cur.execute("SELECT * FROM pelis INNER JOIN reco ON pelis.ID = reco.idpel ORDER BY reco.id;")
        rows = cur.fetchall()
        cur.execute('delete from reco;')
        conn.commit()
        conn.close()
        dolist(rows,False,zid)
    else:
        lista_random(idgen)

def play_video(server,user,cole,pel,pid,tit):
    cinecrypt.play_video(server,user,cole,pel,tit,pid,base)

def router(paramstring):
    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'genero':
            list_genero()
        if params['action'] == 'genero2':
            list_genero2(params['idgen'])
        if params['action'] == 'tema':
            list_tema()
        if params['action'] == 'tema2':
            list_tema2(params['idtem'])
        elif params['action'] == 'anno':
            list_anno()
        elif params['action'] == 'anno2':
            list_anno2(params['anno'])
        elif params['action'] == 'grupo':
            list_grupo()
        elif params['action'] == 'grupo2':
            list_grupo2(params['idgru'])
        elif params['action'] == 'bustit':
            busca_por_titulo()
        elif params['action'] == 'busdir':
            busca_por_director()
        elif params['action'] == 'busdir2':
            busca_por_director2(params['director'])
        elif params['action'] == 'busact':
            busca_por_actor()
        elif params['action'] == 'busact2':
            busca_por_actor2(params['idact'])
        elif params['action'] == 'busgru':
            busca_por_grupo()
        elif params['action'] == 'ultim':
            ultimas()
        elif params['action'] == 'ultim2':
            ultimas2()
        elif params['action'] == 'pelrec':
            peli_recomendada()
        elif params['action'] == 'pelrec2':
            peli_recomendada2(params['idgen'])
        elif params['action'] == 'play':
            play_video(params['server'],params['user'],params['cole'],params['peli'],params['id'],params['tit'])
    else:
        list_categories()

if __name__ == '__main__':
    router(sys.argv[2][1:])




