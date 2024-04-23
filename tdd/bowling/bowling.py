class Juego:
    def __init__(self):
        self._tiros = []
        self._tiros_parciales = 0
        self._indices_spares = []
        self._indices_strikes = []

    def tirar(self, pinos):
        self._tiros.append(pinos)
        self._tiros_parciales += 1
        if self._tiros_parciales == 1 and pinos == 10:  # strike
            self._indices_strikes.append(len(self._tiros))
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
        if self._indices_strikes:
            for idx in self._indices_strikes:
                    score += self._tiros[idx] + self._tiros[idx + 1]
        return score
