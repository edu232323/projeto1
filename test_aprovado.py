from aprovado2 import aprovado

def test1():
    assert aprovado(10, 80, 0) == "Aprovado"

def test2():
    assert aprovado(7, 80, 80) =="Reprovado por faltas"
