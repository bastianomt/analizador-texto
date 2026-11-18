# analizador-texto

CLI en Python que lee un fichero de texto y muestra qué palabras se repiten más.

Proyecto de práctica: solo librería estándar (`re`, `collections`, `pathlib`, `argparse`) y `pytest` para los tests.

## Qué hace

- Normaliza el texto: minúsculas, sin signos de puntuación, respetando tildes y ñ.
- Muestra las N palabras más frecuentes.
- Muestra el total de palabras y cuántas son distintas.
- Opcionalmente ignora las palabras vacías ("de", "la", "y"...).
- Avisa con un mensaje claro si no hay palabras, si ninguna se repite o si la ruta no es válida.

## Requisitos

- Python 3.12 o superior
- [uv](https://docs.astral.sh/uv/)

## Instalación

```bash
git clone https://github.com/<tu_usuario>/analizador-texto.git
cd analizador-texto
uv sync
```

## Uso

```bash
uv run analizador-texto RUTA [--top N] [--sin-vacias]
```

| Argumento      | Descripción                                         |
| -------------- | --------------------------------------------------- |
| `RUTA`         | Fichero de texto a analizar (obligatorio)           |
| `--top N`      | Cuántas palabras mostrar (por defecto 10, mínimo 1) |
| `--sin-vacias` | Ignora las palabras vacías                          |

### Ejemplo

Con un fichero `texto.txt` que contiene `El perro y el gato y el perro.`:

```bash
uv run analizador-texto texto.txt --top 3
```

```
Analizando ruta: texto.txt
Top palabras:
el --> 3
perro --> 2
y --> 2
Total de palabras: 8
Palabras distintas: 4
```

Ignorando las palabras vacías:

```bash
uv run analizador-texto texto.txt --sin-vacias
```

```
Analizando ruta: texto.txt
Top palabras:
perro --> 2
gato --> 1
Total de palabras: 3
Palabras distintas: 2
```

## Tests

```bash
uv run pytest
```

## Estructura

```
analizador-texto/
├── src/analizador_texto/
│   ├── analisis.py   # lógica: normalizar, contar, quitar vacías
│   └── cli.py        # interfaz de consola (argparse)
├── tests/
│   └── test_analisis.py
├── data/sample/      # fichero de ejemplo
├── pyproject.toml
└── uv.lock
```

La lógica está separada de la interfaz: `analisis.py` no sabe nada de la consola, así que se puede probar directamente.

## Limitaciones

- La lista de palabras vacías es pequeña y fija (en español).
- Los números cuentan como palabras y las palabras con guion se separan (`año-2026` → `año`, `2026`).
- El fichero debe estar en UTF-8.
