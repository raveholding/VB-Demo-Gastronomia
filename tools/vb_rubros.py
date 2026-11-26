"""Demo de Gastronomía de Vincular Business · un rubro por carpeta.
Toma el index.html ya armado (marca «Mi Pizzería», tools/vb_gastro.py) y publica:
  /              → Restaurante (la entrada por defecto; con ?rubro=<clave> salta a la carpeta del rubro)
  /parrilla/ /cafeteria/ /bar/ /pizzeria/ /foodtruck/ /cadena/ /darkkitchen/
Cada carpeta lleva su nombre, logo, colores, íconos de la app y su propia base de datos de ejemplo en el navegador.
La carta, las fichas técnicas y las pantallas de cada rubro están en fuente/capa-pizzeria/p11d-gr-datos.js y p11e-gr-ui.js.
Uso: python3 tools/vb_rubros.py   (desde la raíz del repositorio, después de tools/build.sh)"""
import os,re,io,json,base64,shutil,asyncio
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
KEYS=['restaurante','parrilla','cafeteria','bar','pizzeria','foodtruck','cadena','darkkitchen']
# nombre, título del logo, slogan, subtítulo, acento, acento oscuro, acento claro, tamaños (g, i), ícono del logo
W='#ffffff'
ICON={
 'restaurante':'<circle cx="300" cy="215" r="92" fill="none" stroke="ACC" stroke-width="16"/><circle cx="300" cy="215" r="60" fill="none" stroke="#fff" stroke-width="8"/><path d="M170 140 v70 M150 140 v50 a20 20 0 0 0 40 0 v-50 M170 210 v100" stroke="#fff" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M430 140 q-30 30 -10 90 h10 v80" stroke="#fff" stroke-width="12" stroke-linecap="round" fill="none"/>',
 'parrilla':'<path d="M300 110 q60 60 30 120 q40 -20 40 -60 q50 70 -10 130 h-120 q-60 -60 -10 -130 q0 40 40 60 q-30 -60 30 -120z" fill="ACC"/><path d="M190 300 h220" stroke="#fff" stroke-width="14" stroke-linecap="round"/><path d="M210 330 h180" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".8"/>',
 'cafeteria':'<path d="M200 190 h170 v70 a70 70 0 0 1 -70 70 h-30 a70 70 0 0 1 -70 -70z" fill="ACC"/><path d="M370 210 a36 36 0 0 1 0 72" fill="none" stroke="ACC" stroke-width="16"/><path d="M180 345 h220" stroke="#fff" stroke-width="12" stroke-linecap="round"/><path d="M250 170 q-20 -25 0 -50 q20 -25 0 -50 M300 170 q-20 -25 0 -50 q20 -25 0 -50" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" transform="translate(0 20)"/>',
 'bar':'<path d="M200 120 h200 l-100 120z" fill="ACC"/><path d="M300 240 v90 M250 335 h100" stroke="#fff" stroke-width="14" stroke-linecap="round"/><path d="M200 120 h200" stroke="#fff" stroke-width="10" stroke-linecap="round"/><circle cx="395" cy="118" r="26" fill="none" stroke="#fff" stroke-width="10"/>',
 'foodtruck':'<rect x="150" y="160" width="210" height="130" rx="14" fill="ACC"/><path d="M360 200 h60 l40 50 v40 h-100z" fill="#fff"/><rect x="180" y="185" width="150" height="40" rx="6" fill="#0d0d0d"/><circle cx="215" cy="300" r="30" fill="#0d0d0d" stroke="#fff" stroke-width="10"/><circle cx="400" cy="300" r="30" fill="#0d0d0d" stroke="#fff" stroke-width="10"/>',
 'cadena':'<path d="M150 210 l30 -70 h240 l30 70z" fill="ACC"/><rect x="170" y="210" width="260" height="120" rx="8" fill="none" stroke="#fff" stroke-width="12"/><rect x="270" y="250" width="60" height="80" fill="#fff"/><text x="300" y="196" font-family="DejaVu Sans,Arial" font-weight="700" font-size="46" fill="#0d0d0d" text-anchor="middle">x3</text>',
 'darkkitchen':'<path d="M210 220 a50 50 0 0 1 20 -95 a70 70 0 0 1 140 0 a50 50 0 0 1 20 95z" fill="#fff"/><rect x="215" y="220" width="170" height="90" rx="10" fill="ACC"/><path d="M240 260 h120 M240 285 h80" stroke="#0d0d0d" stroke-width="10" stroke-linecap="round"/>'}
R={
 'restaurante':dict(n='Mi Restaurante',t='MI RESTAURANTE',slogan='Cocina de autor y platos de siempre · Salta',sub='Cocina de autor y platos de siempre',acc='#e0912b',dk='#9a5b0c',lt='#f3b25e',sz=('Plato completo','Media porción')),
 'parrilla':dict(n='Mi Parrilla',t='MI PARRILLA',slogan='Parrilla y bodegón · Salta',sub='Parrilla y bodegón',acc='#e2412b',dk='#a1220f',lt='#f2775f',sz=('Porción completa','Media porción')),
 'cafeteria':dict(n='Mi Café',t='MI CAFÉ',slogan='Café de especialidad y panadería · Salta',sub='Café de especialidad y panadería',acc='#c8874a',dk='#7a4b1f',lt='#e2ac78',sz=('Grande','Chico')),
 'bar':dict(n='Mi Bar',t='MI BAR',slogan='Bar de tragos y cervecería · Salta',sub='Bar de tragos y cervecería',acc='#a78bfa',dk='#6d28d9',lt='#c4b5fd',sz=('Doble','Simple')),
 'pizzeria':None,
 'foodtruck':dict(n='Mi Food Truck',t='MI FOOD TRUCK',slogan='Comida callejera en ferias y eventos · Salta',sub='Comida callejera en ferias y eventos',acc='#f2c12e',dk='#a37d00',lt='#f7d873',sz=('Doble','Simple')),
 'cadena':dict(n='Mi Cadena',t='MI CADENA',slogan='Hamburguesería con 3 sucursales · Salta',sub='Hamburguesería · 3 sucursales',acc='#38bdf8',dk='#0369a1',lt='#7dd3fc',sz=('Doble','Simple')),
 'darkkitchen':dict(n='Mi Dark Kitchen',t='MI DARK KITCHEN',slogan='Tres marcas, una sola cocina · Salta',sub='Tres marcas, una sola cocina · sólo delivery y retiro',acc='#34d399',dk='#047857',lt='#6ee7b7',sz=('Grande','Chico'))}
def logo_svg(k,r):
    t=r['t'];fs=68 if len(t)<=7 else 58 if len(t)<=10 else 48 if len(t)<=13 else 42
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600"><circle cx="300" cy="300" r="296" fill="#0d0d0d"/><circle cx="300" cy="300" r="258" fill="none" stroke="{r['acc']}" stroke-width="10"/>
{ICON[k].replace('ACC',r['acc'])}<text x="300" y="425" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="{fs}" fill="#fff" text-anchor="middle">{t}</text>
<text x="300" y="478" font-family="DejaVu Sans,Arial,sans-serif" font-weight="700" font-size="25" fill="{r['acc']}" text-anchor="middle" letter-spacing="1">GASTRONOMÍA · DEMO</text></svg>'''
async def render(svgs):
    from playwright.async_api import async_playwright
    out={}
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':600,'height':600})
        for k,s in svgs.items():
            await pg.set_content('<html><body style="margin:0;background:transparent">'+s+'</body></html>');out[k]=await pg.screenshot(omit_background=True,clip={'x':0,'y':0,'width':600,'height':600})
        await b.close()
    return out
def uris(png):
    im=Image.open(io.BytesIO(png)).convert('RGBA')
    b=io.BytesIO();im.save(b,'WEBP',quality=90);menu='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
    g=Image.new('RGB',im.size,'#0b0a0a');g.paste(im,(0,0),im);g=g.convert('L');Wt=384;H=round(g.height*Wt/g.width);g=g.resize((Wt,H),Image.LANCZOS)
    bw=g.point(lambda v:0 if v>100 else 255).convert('1');b=io.BytesIO();bw.save(b,'PNG',optimize=True);ticket='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    ic=Image.new('RGB',im.size,'#0b0a0a');ic.paste(im,(0,0),im);b=io.BytesIO();ic.resize((180,180),Image.LANCZOS).save(b,'PNG',optimize=True);icon='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
    return menu,ticket,icon,im
def app_icons(im,d):
    for n,mask in [(180,0),(192,0),(512,0),(512,1)]:
        c=Image.new('RGB',(n,n),'#0b0a0a');w=int(n*(.74 if mask else .96));l=im.resize((w,w),Image.LANCZOS);c.paste(l,((n-w)//2,(n-w)//2),l)
        c.save(os.path.join(d,'app-%d%s.png'%(n,'m' if mask else '')),optimize=True)
base=open('index.html',encoding='utf8').read()
assert 'GR_KEY' in base,'falta la capa de rubros (p11d/p11e) en el index.html'
def cval(name):
    m=re.search(r'const %s="([^"]*)"'%name,base);assert m,name;return m.group(1)
L_MENU,L_TICKET=cval('LOGO_MENU'),cval('LOGO_TICKET')
m=re.search(r'<link rel="icon" href="([^"]*)"',base);L_ICON=m.group(1)
svgs={k:logo_svg(k,r) for k,r in R.items() if r}
pngs=asyncio.run(render(svgs))
HEAD_AT='window.RAVE_CLOUD='
def variant(k):
    r=R[k];h=base;sub=k!='restaurante'
    rootp='../' if sub else './'
    acc=r['acc'] if r else '#ff7f00'
    inj=('<script>(function(){var K=%s,ROOT=%s,me=%s;try{var q=new URLSearchParams(location.search).get("rubro");if(q&&q!==me&&K.indexOf(q)>=0){location.replace(ROOT+(q==="restaurante"?"":q+"/")+location.hash);return;}}catch(e){}'
         'window.VB_GR=me;window.VB_GR_ROOT=ROOT;window.VB_GR_ACC=%s;window.RAVE_BUILD.db="vb-demo-gastronomia-v1-"+me;})();</script>\n')%(json.dumps(KEYS),json.dumps(rootp),json.dumps(k),json.dumps(acc))
    i=h.find('</script>',h.find(HEAD_AT));assert i>0
    h=h[:i+9]+'\n'+inj+h[i+9:]
    if r:
        menu,ticket,icon,im=uris(pngs[k])
        assert h.count(L_MENU)>=2
        h=h.replace(L_MENU,menu).replace(L_TICKET,ticket).replace(L_ICON,icon)
        N=r['n']
        for a,b in [('Pizza Mi Pizzería · Grande',N+' · plato de ejemplo'),('Mi Pizzería Pizzeria',N),('Mi Pizzería de masa madre',N),('Pizzería de masa madre · Salta',r['slogan']),('Pizzería de masa madre',r['sub']),
                    ('MI PIZZERÍA',r['t']),('Club Mi Pizz"','Club "'),('Mi Pizzería',N),("'Grande · 8 porciones'","'"+r['sz'][0]+"'"),('Una pizzería vende al consumidor final','Un comercio gastronómico vende al consumidor final'),
                    ('#ff7f00',r['acc']),('#ff9a3d',r['lt']),('#b84f00',r['dk']),('#ffb066',r['lt']),('#ffd9b0',r['lt'])]:
            h=h.replace(a,b)
        h=h.replace("'Grande · 8 porciones'","'"+r['sz'][0]+"'")
        for w in ['Mi Pizzería','MI PIZZERÍA']:assert w not in h,(k,w)
    return h
def write_dir(k,h):
    d='.' if k=='restaurante' else k
    os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf8').write(h)
    if d!='.':
        for f in ['sw.js']:shutil.copy(f,os.path.join(d,f))
    r=R[k]
    for f in ['app.webmanifest','club.webmanifest']:
        s=open(f,encoding='utf8').read() if d=='.' else open(os.path.join('.',f),encoding='utf8').read()
        if r:s=s.replace('Mi Pizzería',r['n']).replace('MI PIZZERÍA',r['t']).replace('#ff7f00',r['acc'])
        open(os.path.join(d,f),'w',encoding='utf8').write(s)
    if r:app_icons(uris(pngs[k])[3],d)
    elif d!='.':
        for f in ['app-180.png','app-192.png','app-512.png','app-512m.png']:shutil.copy(f,os.path.join(d,f))
# primero las carpetas (copian los archivos de la raíz con la marca de la pizzería), al final la raíz (restaurante)
os.makedirs('pizzeria',exist_ok=True)
for f in ['app.webmanifest','club.webmanifest','app-180.png','app-192.png','app-512.png','app-512m.png']:shutil.copy(f,os.path.join('pizzeria',f))
for k in KEYS:
    if k=='restaurante':continue
    write_dir(k,variant(k));print('rubro',k,'ok')
write_dir('restaurante',variant('restaurante'));print('rubro restaurante (raíz) ok')
for k,r in R.items():
    if r:open(os.path.join('fuente','build','logo-%s.png'%k) if os.path.isdir('fuente/build') else '/tmp/logo-%s.png'%k,'wb').write(pngs[k])
