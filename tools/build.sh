#!/bin/sh
# Compila la demo de Gastronomía: fuente de la pizzería + marca genérica de Vincular Business.
set -e
cd "$(dirname "$0")/../fuente"
PUBLIC_URL=https://raveholding.github.io/VB-Demo-Gastronomia/ python3 build.py pizza ../index.html
cd ..
python3 tools/vb_gastro.py index.html
python3 tools/vb_gastro.py app.webmanifest
python3 tools/vb_gastro.py club.webmanifest
python3 tools/vb_gastro.py sw.js
