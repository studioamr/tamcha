#!/usr/bin/env python3
"""TAMCHA - genera imagenes de marca con Gemini (Nano Banana Pro).

Uso:
  export GEMINI_API_KEY="tu_key"   # la misma que usas en monster-kebabs
  /usr/local/bin/python3 herramientas/gen_imagenes.py

Guarda en img/ las piezas que el deck no tiene (matcha verde, bodegon hero).
Las referencias de estilo salen de los recortes reales del deck en img/.
"""
import os, sys, pathlib

if not os.environ.get("GEMINI_API_KEY"):
    sys.exit("Exporta GEMINI_API_KEY primero (misma key de monster-kebabs).")

from google import genai
from google.genai import types
from PIL import Image

RAIZ = pathlib.Path(__file__).resolve().parent.parent
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

ESTILO = ("Match exactly the brand photography style of the reference images: "
          "matte black brutalist scene, warm sepia-beige tones, brushed steel and "
          "volcanic stone surfaces, one precise warm LED light strip, deep shadows, "
          "editorial product photography, 85mm lens, shallow depth of field. "
          "The brand wordmark TAMCHA with a small four-pointed sparkle may appear "
          "engraved subtly. No people, no text overlays, no watermark graphics.")

PIEZAS = [
    ("hero-bodegon.jpg", "21:9", "2K",
     "Ultra-wide still life: chunky silver .925 rings and a heavy silver curb chain "
     "arranged on a volcanic stone slab next to a matte black ceramic cup engraved "
     "TAMCHA filled with a vivid green matcha latte with latte art. " + ESTILO),
    ("matcha-latte.jpg", "4:5", "2K",
     "Close-up of a vivid green ceremonial matcha latte in a matte black TAMCHA "
     "ceramic cup on a brushed steel counter, soft steam, dark cafe background. " + ESTILO),
    ("plata-macro.jpg", "4:5", "2K",
     "Extreme macro: stack of hammered silver .925 rings, one with black onyx stone, "
     "and a silver chain draped over rough volcanic stone. " + ESTILO),
]

refs = [Image.open(RAIZ / "img" / f) for f in
        ("linea-joyeria.jpg", "taza-osito-barra.jpg", "interior-vitrinas.jpg")]

for nombre, ratio, tam, prompt in PIEZAS:
    print(f"Generando {nombre} ({ratio}, {tam})...")
    r = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=[prompt, *refs],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=ratio, image_size=tam),
        ),
    )
    for part in r.parts:
        if part.inline_data:
            part.as_image().save(RAIZ / "img" / nombre)
            print("  ->", RAIZ / "img" / nombre)
            break
    else:
        print("  !! sin imagen en la respuesta:", getattr(r, "text", "")[:200])
print("Listo. Revisa img/ e integra en index.html donde quieras.")
