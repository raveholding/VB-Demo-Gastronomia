# Gastronomía · Sistema VB (demo de Vincular Business)

Demo genérica para restaurantes, parrillas, cafeterías, bares, pizzerías, food trucks, cadenas y dark kitchens, armada sobre la misma aplicación de la demo de pizzería (capa `pizza` del Sistema VB) con la marca **Mi Pizzería**.

**Demo en línea:** https://raveholding.github.io/VB-Demo-Gastronomia/

- Carta pública (retiro y delivery): `/`
- Carta de una mesa (QR o tag NFC): `/?mesa=I4`
- Acceso del equipo: `/#acceso` · ADMIN 1234 · Supervisor 1111 · Caja 0000 · Mozo 2222 · Moza 3333 · Barra 4444 · Cocina 5555 · Cadete 8888

Incluye salón y barra con mapa de mesas, mozo, comandas (Mesa → Mozo → Caja → Cocina → Listo → Servido), cocina, delivery y PedidosYa simulado, fermentación, fichas técnicas con descuento de insumos, Club de clientes, caja, RRHH y el diseño para celular (barra inferior por perfil).

**Es una demo:** carta, precios, personal y ventas son de ejemplo y se guardan sólo en el navegador. Los mensajes de WhatsApp van a Vincular Business.

## Rubros (V27.36)
La misma demo armada para 8 tipos de negocio, cada uno en su carpeta, con su carta, fichas técnicas, logo y colores:

| Rubro | Dirección |
| --- | --- |
| Restaurante | `/` |
| Parrilla y bodegón | `/parrilla/` |
| Cafetería | `/cafeteria/` |
| Bar y cervecería | `/bar/` |
| Pizzería y delivery | `/pizzeria/` |
| Food truck y ferias | `/foodtruck/` |
| Cadena multisucursal | `/cadena/` (3 sucursales con consolidado de cajas) |
| Dark kitchen | `/darkkitchen/` (3 marcas, sin salón) |

También funciona `/?rubro=bar` (salta a la carpeta). Cada rubro guarda sus datos de ejemplo por separado en el navegador.
La carta de cada rubro está en `fuente/capa-pizzeria/p11d-gr-datos.js`; ilustraciones y selector en `p11e-gr-ui.js`; carpetas y logos en `tools/vb_rubros.py`.

## Cómo se compila
```
sh tools/build.sh
```
`fuente/` es la fuente del Sistema VB con la capa de pizzería; `tools/vb_gastro.py` cambia sólo la presentación (nombre, contacto, correos, claves de almacenamiento) para que no se mezcle con la demo del cliente.

Desarrollado por **VINCULAR BUSINESS** · Celular (387) 4484132 · https://www.vincularbusiness.com.ar/ · vincularbusiness@gmail.com · *“Tu idea, en buenas manos.”*
