from Poo.M06_TP02.AspirateurRobot import AspirateurRobot

ar = AspirateurRobot("Dyson", 7500, 50)
ar.avancer(5)
ar.tourner(1)
ar.avancer(4)
print(ar)
print(ar.numero_serie)