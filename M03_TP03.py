total_grains = 0
grains = 1

for ligne in range(1, 9):
    for colonne in range(1, 9):
        print(f"Ligne {ligne}, Colonne {colonne} → {grains} grains")
        total_grains += grains
        grains *= 2

print(f"Total des grains de riz : {total_grains}")
