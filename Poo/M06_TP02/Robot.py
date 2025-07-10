import random
import string

class Robot:
    _nb_robots = 0
    _orientations = ["NORD", "EST", "SUD", "OUEST"]
    _statuts_valides = {1: "EN SERVICE", 2: "HORS SERVICE", 3: "EN RÉPARATION"}

    def __init__(self, robot_type="Générique"):
        self.robot_type = robot_type
        self.__numero_serie = self._generer_numero_serie()
        self._orientation = "NORD"
        self._statut = 1
        Robot._nb_robots += 1

    @staticmethod
    def _generer_numero_serie():
        lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
        chiffres = str(random.randint(0, 9999999999)).zfill(10)
        return lettres + chiffres

    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, val):
        if isinstance(val, str) and len(val) >= 2:
            self._robot_type = val
        else:
            print("Type invalide, valeur par défaut appliquée.")
            self._robot_type = "Générique"

    @property
    def numero_serie(self):
        return self.__numero_serie

    @property
    def orientation(self):
        return self._orientation

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self, val):
        if val in Robot._statuts_valides:
            self._statut = val
        else:
            print("Statut invalide.")

    def __str__(self):
        return f"""Robot {self.__numero_serie} – {self.robot_type}
Statut : {Robot._statuts_valides[self._statut]}
Orientation : {self._orientation}"""

    def tourner(self, direction):
        if direction not in [1, -1]:
            print("Direction invalide, utilisez 1 (horaire) ou -1 (anti-horaire)")
            return
        idx = Robot._orientations.index(self._orientation)
        self._orientation = Robot._orientations[(idx + direction) % 4]
