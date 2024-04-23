class Juego:
    def __init__(self):
        self._score = 0

    def tirar(self, pinos):
        self._score += pinos

    def score(self):
        return self._score
