import argparse
from pathlib import Path

from analizador_texto import analisis


def main() -> None:
    parser = argparse.ArgumentParser(description="Analizador de texto")
    parser.add_argument("ruta", type=Path, help="Ruta del archivo de texto a analizar")
    args = parser.parse_args()
    
    print(args.ruta)

    fichero_a_leer = args.ruta.read_text(encoding="utf-8")
    texto_normalizado = analisis.normalizar(fichero_a_leer)
    texto_sin_vacias = analisis.quitar_vacias(texto_normalizado)
    palabras_mas_repetidas = analisis.top_palabras(texto_sin_vacias)
    print(f"Top palabras: {palabras_mas_repetidas}")

    for palabra, veces in palabras_mas_repetidas:
        print(f"{palabra}: {veces}")    


