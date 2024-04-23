from bowling import Juego


def test_perdedor():
    j = Juego()
    for i in range(20):
        j.tirar(0)
    assert j.score() == 0
