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
    j = Juego()
    for i in range(20):
        if i == 10:
            j.tirar(0)
        elif i == 11:
            j.tirar(10)
        else:
            j.tirar(1)
    assert j.score() == 29


def test_strike():
    j = Juego()
    for i in range(19):
        if i == 8:
            j.tirar(10)
        else:
            j.tirar(1)
    assert j.score() == 30
