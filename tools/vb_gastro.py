"""Demo genérica de Gastronomía de Vincular Business, armada sobre la demo de pizzería (capa `pizza`).
Cambia sólo la presentación: nombre, contacto, correos, direcciones y claves de almacenamiento, para que no se mezcle
con la demo del cliente en el mismo navegador. Uso: python3 tools/vb_gastro.py index.html"""
import sys
p=sys.argv[1];h=open(p,encoding='utf8').read()
R=[
 # la pizza de la casa deja de llevar el nombre del cliente
 ("'dp-piz','Di Parma',","'dp-piz','Especial de la casa',"),("Le gusta la Di Parma bien cocida","Le gusta la especial bien cocida"),
 ("Di Parma Pizzería de masa madre","Mi Pizzería de masa madre"),("Di Parma Pizzería","Mi Pizzería"),("DI PARMA","MI PIZZERÍA"),
 ("Club Di Parm\"","Club Mi Pizz\""),("Di Parma","Mi Pizzería"),("DiParma","MiPizzeria"),("Diparma","Mipizzeria"),
 ("diparma.pizza.mp","mipizzeria.mp"),("@diparma.example","@mipizzeria.example"),
 ("rave-diparma-demo-v1","vb-demo-gastronomia-v1"),("svb-diparma-","vb-gastro-"),("rave.theme.diparma","rave.theme.vbgastro"),
 ("DIPARMAPizzeriaDemo","VB-Demo-Gastronomia"),
 # contacto: WhatsApp de Vincular Business; direcciones de ejemplo
 ("5493874574892","5493874484132"),("387 4574892","387 4484132"),
 ("Licoreria RAVE, Urquiza 1052, Salta, Argentina","Av. Ejemplo 123, Salta, Argentina"),("Urquiza 1052, Salta","Av. Ejemplo 123, Salta"),
]
for a,b in R: h=h.replace(a,b)
open(p,'w',encoding='utf8').write(h)
import re
rest=sorted(set(m.group(0) for m in re.finditer(r'.{0,25}[Pp]arma.{0,25}',h)))
print('vb-gastro aplicado; restos de la marca:',len(rest)); [print('  ',x) for x in rest[:20]]
