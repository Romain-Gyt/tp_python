from random import choice


# === Fonctions de base ===

def est_predateur(a, b):
    return (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)


def est_proie(a, b):
    return est_predateur(b, a)


def voisins(grille, x, y):
    res = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
                res.append(grille[nx][ny])
    return res


def maj_centre(grille):
    x, y = 1, 1
    proie = grille[x][y]
    autour = voisins(grille, x, y)

    nb_predateurs = sum(1 for a in autour if est_predateur(a, proie))
    nb_proies = sum(1 for a in autour if est_proie(a, proie))
    nb_neutres = len(autour) - nb_predateurs - nb_proies

    print(f"Proie centrale = {proie}")
    print(f"Voisins : {autour}")
    print(f"Prédateurs : {nb_predateurs}, Proies : {nb_proies}, Neutres : {nb_neutres}")

    if nb_predateurs > len(autour) // 2:
        grille[x][y] = [a for a in autour if est_predateur(a, proie)][0]
        print(" Règle 1 appliquée : remplacé par prédateur")
    elif nb_predateurs < len(autour) // 2:
        print(" Règle 2 appliquée : aucun changement")
    elif nb_predateurs == nb_proies and nb_predateurs > 0:
        if choice([True, False]):
            grille[x][y] = [a for a in autour if est_predateur(a, proie)][0]
            print(" Règle 3 appliquée : 50% chance → remplacé")
        else:
            print(" Règle 3 appliquée : 50% chance → inchangé")
    elif nb_predateurs > 0 and nb_neutres > 0 and nb_predateurs > nb_proies:
        grille[x][y] = [a for a in autour if est_predateur(a, proie)][0]
        print(" Règle 4 appliquée : remplacé par prédateur")


def afficher(grille):
    for ligne in grille:
        print(ligne)
    print()

tests = [
    {
        "nom": "Règle 1 – majorité de prédateurs",
        "grille": [
            [1, 1, 1],
            [2, 2, 1],
            [1, 1, 1]
        ]
    },
    {
        "nom": "Règle 2 – minorité de prédateurs",
        "grille": [
            [3, 3, 3],
            [2, 2, 3],
            [3, 3, 3]
        ]
    },
    {
        "nom": "Règle 3 – égalité entre prédateurs et proies",
        "grille": [
            [1, 3, 3],
            [3, 2, 1],
            [1, 1, 3]
        ]
    },
    {
        "nom": "Règle 4 – majorité de prédateurs et de neutres",
        "grille": [
            [1, 1, 3],
            [3, 2, 3],
            [3, 1, 3]
        ]
    },
]

# === Exécution de tous les cas de test ===

for test in tests:
    print("", test["nom"])
    print("Avant :")
    afficher(test["grille"])
    maj_centre(test["grille"])
    print("Après :")
    afficher(test["grille"])
    print("=" * 40)
