# créez une fonction qui prend en paramètre une suite de longueur indéterminée de int
# et qui renvoi la valeur en bit de la multiplication de ceux ci

def bit_value(*nombres):
    produit = 1
    for n in nombres:
        produit *= n
    return bin(produit)

print(bit_value(1000))