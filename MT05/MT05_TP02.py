import string
from collections import Counter


def nettoyer_texte(texte):

    texte = texte.lower()
    return ''.join(c for c in texte if c in string.ascii_lowercase)

def compter_lettres(texte):
    lettres = {}
    for lettre in nettoyer_texte(texte):
        lettres[lettre] = lettres.get(lettre, 0) + 1
    return lettres

test =   "Chenille"
print(compter_lettres(test))

def est_anagramme(phrase1, phrase2):
    return  "Oui" if compter_lettres(phrase1) == compter_lettres(phrase2)  else "Non"
ex1 = ("Chien", "Niche")
ex2 = ("Pablo Picasso", "Pascal Obispo")
ex3 = ("Albert Einstein", "Rien n’est établi")

for p1, p2 in [ex1, ex2, ex3]:
    print(f"{p1} / {p2} → Anagramme ? {est_anagramme(p1, p2)}")






