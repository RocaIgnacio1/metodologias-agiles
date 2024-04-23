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


def test_spare():
    j = Juego()
    for i in range(20):
        if i == 11:
            j.tirar(9)
        else:
            j.tirar(1)
    assert j.score() == 29
