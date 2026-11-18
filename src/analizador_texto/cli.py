import argparse
from pathlib import Path

from analizador_texto import analisis


def main() -> None:
    parser = argparse.ArgumentParser(description="Analizador de texto")
    parser.add_argument("ruta", type=Path, help="Ruta del archivo de texto a analizar")
    parser.add_argument("--top", type=int, default=10, help="Cuántas palabras mostrar")
    parser.add_argument(
        "--sin-vacias", action="store_true", help="Ignora palabras vacias"
    )
    args = parser.parse_args()

    print(f"Analizando: {args.ruta}")
    texto = args.ruta.read_text(encoding="utf-8")

    texto_normalizado = analisis.normalizar(texto)

    if not texto_normalizado:
        print("El fichero no tiene palabras")
        return

    if args.sin_vacias:
        palabras = analisis.quitar_vacias(texto_normalizado)
    else:
        palabras = texto_normalizado

    if not palabras:
        print("Todas las palabras restantes son vacias")
        return

    top = analisis.top_palabras(palabras, args.top)

    if top[0][1] == 1:
        print("Ninguna palabra se repite")
    else:
        print("Top palabras:")
        for palabra, veces in top:
            print(f"{palabra} --> {veces}")

    print(f"Total de palabras: {len(palabras)}")
    print(f"Palabras distintas: {len(set(palabras))}")
