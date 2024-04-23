from bowling import Juego


def test_perdedor():
    j = Juego()
    for i in range(20):
        j.tirar(0)
    assert j.score() == 0


def test_unos():
    j = Juego()
    for i in range(20):
        j.tirar(1)
    assert j.score() == 20
