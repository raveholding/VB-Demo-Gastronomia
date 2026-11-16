# Gastronomía · Sistema VB (demo de Vincular Business)

Demo genérica para pizzerías, restaurantes y bares, armada sobre la misma aplicación de la demo de pizzería (capa `pizza` del Sistema VB) con la marca **Mi Pizzería**.

**Demo en línea:** https://raveholding.github.io/VB-Demo-Gastronomia/

- Carta pública (retiro y delivery): `/`
- Carta de una mesa (QR o tag NFC): `/?mesa=I4`
- Acceso del equipo: `/#acceso` · ADMIN 1234 · Supervisor 1111 · Caja 0000 · Mozo 2222 · Moza 3333 · Barra 4444 · Cocina 5555 · Cadete 8888

Incluye salón y barra con mapa de mesas, mozo, comandas (Mesa → Mozo → Caja → Cocina → Listo → Servido), cocina, delivery y PedidosYa simulado, fermentación, fichas técnicas con descuento de insumos, Club de clientes, caja, RRHH y el diseño para celular (barra inferior por perfil).

**Es una demo:** carta, precios, personal y ventas son de ejemplo y se guardan sólo en el navegador. Los mensajes de WhatsApp van a Vincular Business.

## Cómo se compila
```
sh tools/build.sh
```
`fuente/` es la fuente del Sistema VB con la capa de pizzería; `tools/vb_gastro.py` cambia sólo la presentación (nombre, contacto, correos, claves de almacenamiento) para que no se mezcle con la demo del cliente.

Desarrollado por **VINCULAR BUSINESS** · Celular (387) 4484132 · https://www.vincularbusiness.com.ar/ · vincularbusiness@gmail.com · *“Tu idea, en buenas manos.”*
