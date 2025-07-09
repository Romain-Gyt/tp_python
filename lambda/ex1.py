from functools import reduce

taux_interets = [1.2, 1.4, 2.5, 3.6, 4.7, 1.8, 2.9, 2.0] 


multiplicateurs = [1 + taux / 100 for taux in taux_interets]


facteur_total = reduce(lambda x, y: x * y, multiplicateurs)


montant_initial = 1000
montant_final = montant_initial * facteur_total

print(f"Montant après 8 ans : {montant_final:.2f} €")
