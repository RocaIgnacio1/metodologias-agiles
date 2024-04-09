"""
int Sumar(string numeros):

1. El método puede tomar uno, dos números enteros o más, separados por coma.
   Un string vacío suma 0.

Ejemplos: "1,2"=3 "4,2"=6 ""=0 "3,8,7"=18

2. También admite nuevas líneas: "\n"

Ejemplo: "1,2,4\n5,6"=18

3. El delimitador es configurable si se agrega //[delimitador]\n al principio.

Ejemplo: "//;\n1;3;6;4"=14
Ejemplo: "//|\n1|3|6|4"=14

4. Enviar un número negativo dispara una Excepción con el mensaje “no se permiten negativos” y el número negativo incluido en el mensaje.
"""

from modulo import sumar


def test_sumar_vacio():
    numeros = ""
    assert sumar(numeros) == 0


def test_sumar_uno():
    numero = "7"
    assert sumar(numero) == 7


def test_sumar_dos_comas():
    numeros = "5,3"
    assert sumar(numeros) == 8
    numeros = "8,7"
    assert sumar(numeros) == 15


def test_sumar_tres_comas():
    numeros = "3,8,7"
    assert sumar(numeros) == 18
    numeros = "3,8,9"
    assert sumar(numeros) == 20
