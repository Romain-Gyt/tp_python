class Aspirateur:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, val):
        self._marque = val

    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, val):
        self._puissance = val

    def __str__(self):
        return f"Aspirateur {self.marque}, puissance={self.puissance}W"
