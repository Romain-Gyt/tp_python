import random

def est_predateur(a, b):
    return (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)

def est_proie(a, b):
    return est_predateur(b, a)

grille = [
    [1, 3, 2],
    [1, 2,1 ],
    [3, 2, 1]
]

def afficher_grille(g):
    for ligne in g:
        print(" ".join(str(x) for x in ligne))

def mise_a_jour(grille):
    centre = grille[1][1]
    nb_predateurs = 0
    nb_proies = 0
    nb_autres = 0

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            voisin = grille[i][j]
            if est_predateur(voisin, centre):
                nb_predateurs += 1
            elif est_proie(voisin, centre):
                nb_proies += 1
            else:
                nb_autres += 1
    print("nb_predateurs: " + str(nb_predateurs))
    print("nb_proies: " + str(nb_proies))
    print("nb_autres: " + str(nb_autres))

    if nb_predateurs >= 4:
        grille[1][1] = get_predateur(centre)
    elif nb_predateurs < 4:
        pass
    elif nb_predateurs == 4 and nb_proies == 4:
        if random.choice([True, False]):
            grille[1][1] = get_predateur(centre)
    elif nb_predateurs == 4 and nb_autres == 4:
        grille[1][1] = get_predateur(centre)

def get_predateur(animal):
    if animal == 1:
        return 3
    elif animal == 2:
        return 1
    elif animal == 3:
        return 2



print("---------- Avant ----------")
afficher_grille(grille)

mise_a_jour(grille)

print("---------- Après ----------")
afficher_grille(grille)
