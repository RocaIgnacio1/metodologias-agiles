class Juego:
    def __init__(self):
        self._tiros = []
        self._tiros_parciales = 0
        self._indices_spares = []

    def tirar(self, pinos):
        self._tiros.append(pinos)
        self._tiros_parciales += 1
        if self._tiros_parciales == 2:
            self._tiros_parciales = 0
            if self._tiros[-2] + self._tiros[-1] == 10:
                self._indices_spares.append(len(self._tiros))

    def score(self):
        score = sum(self._tiros)
        if self._indices_spares:
            for idx in self._indices_spares:
                if idx < len(self._tiros):
                    score += self._tiros[idx]
        return score
