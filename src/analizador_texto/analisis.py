import re
from collections import Counter

PALABRAS_VACIAS = {"de", "la", "el", "y", "en", "un", "una", "con", "a", "los", "las"}


def normalizar(texto: str) -> list[str]:
    """Devuelve las palabras del texto en minusculas y sin puntuacion"""
    texto = texto.lower()
    return re.findall(r"\w+", texto)


def top_palabras(palabras: list[str], n: int = 10) -> list[tuple[str, int]]:
    contador = Counter(palabras)
    return contador.most_common(n)


def quitar_vacias(palabras: list[str]) -> list[str]:
    return [palabra for palabra in palabras if palabra not in PALABRAS_VACIAS]


def main() -> None:
    texto = "Aquí hay un ejemplo de texto con varias palabras, algunas en mayúsculas y otras en minúsculas."

    palabras = normalizar(texto)
    print(f"listado de palabras \n\t {palabras}")

    lista_sin_vacias = quitar_vacias(palabras)
    print(f"listado de palabras sin vacías \n\t {lista_sin_vacias}")

    palabras_comunes = top_palabras(lista_sin_vacias)
    print(f"listado de palabras comunes \n\t {palabras_comunes}")


if __name__ == "__main__":
    main()
