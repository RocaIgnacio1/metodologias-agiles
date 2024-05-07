from funciones import sumar, multiplicar

def test_sumar():
    assert sumar(5,6) == 11
    assert sumar(0,0) == 0
    assert sumar(-1,-1) == -2
 
 
def test_multiplicar():
    assert multiplicar(5,6) == 30
    assert multiplicar(0,0) == 0
    assert multiplicar(-1,-1) == 1