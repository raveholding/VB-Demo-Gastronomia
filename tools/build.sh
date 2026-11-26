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
python3 tools/vb_rubros.py
for f in index.html */index.html; do case "$f" in fuente/*|tools/*) continue;; esac; python3 tools/vb_guia.py gastronomia "$f" >/dev/null; done
