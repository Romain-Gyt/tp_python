from Poo.M06_TP02.Robot import Robot


class RobotMobile(Robot):
    def __init__(self, robot_type="Générique", abs=0, ord=0):
        super().__init__(robot_type)
        self._abscisse = abs
        self._ordonnee = ord

    @property
    def abscisse(self):
        return self._abscisse

    @property
    def ordonnee(self):
        return self._ordonnee

    def afficher_position(self):
        return f"Position : [abs={self._abscisse} ; ord={self._ordonnee}]"

    def avancer(self, m):
        if self.orientation == "EST":
            self._abscisse += m
        elif self.orientation == "OUEST":
            self._abscisse -= m
        elif self.orientation == "NORD":
            self._ordonnee += m
        elif self.orientation == "SUD":
            self._ordonnee -= m

    def __str__(self):
        base = super().__str__()
        return f"{base}\n{self.afficher_position()}"
