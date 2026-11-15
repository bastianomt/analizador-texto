from analizador_texto import analisis


def test_normalizar_v1():
    assert analisis.normalizar("Hola, mundo!") == ["hola", "mundo"]


def test_normalizar_v2():
    assert analisis.normalizar("") == []


def test_top_palabras():
    assert analisis.top_palabras(["hola", "de", "hola"], 1) == [("hola",2)]


def test_quitar_vacias():
    assert analisis.quitar_vacias(["hola", "de", "mundo", "y"]) == ["hola", "mundo"]