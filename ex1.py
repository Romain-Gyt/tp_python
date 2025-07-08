def calcul_salaire_journalier(nb_heures, taux_horaire):
    salaire = 0

    heures_normales = min(nb_heures, 8)
    salaire += heures_normales * taux_horaire

    if nb_heures > 8:
        heures_25 = min(nb_heures - 8, 3)
        salaire += heures_25 * taux_horaire * 1.25

    if nb_heures > 11:
        heures_50 = nb_heures - 11
        salaire += heures_50 * taux_horaire * 1.5

    return salaire

print(calcul_salaire_journalier(10, 15))