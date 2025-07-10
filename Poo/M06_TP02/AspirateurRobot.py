from Poo.M06_TP02.Aspirateur import Aspirateur
from Poo.M06_TP02.RobotMobile import RobotMobile


class AspirateurRobot(Aspirateur, RobotMobile):
    def __init__(self, marque, puissance, distance_max):
        Aspirateur.__init__(self, marque, puissance)
        RobotMobile.__init__(self, "Aspirateur robot")
        self.distance_max = distance_max

    @property
    def distance_max(self):
        return self._distance_max

    @distance_max.setter
    def distance_max(self, val):
        self._distance_max = val

    def __str__(self):
        base = RobotMobile.__str__(self)
        return f"""{base}
Marque : {self.marque}
Puissance : {self.puissance}W"""
