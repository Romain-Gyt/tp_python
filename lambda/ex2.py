#soit la liste d'élèves suivante
eleves = [
    "Thomas", "Bertrand", "Marie", "Etienne", "Jean", "Arnaud", "Bertrand", "Xavier", "Martin", "Jeanne",
    "David", "Rodolphe", "Genevieve", "Pierre", "Karim", "Ines", "Adrien", "Magalie", "Romaric", "Antoine",
    "Karim", "Ines", "Adrien", "Sofia", "Mehdi", "Clara", "Julien", "Amira", "Lucas", "Sarah", "Nicolas",
    "Leïla", "Thomas", "Amina", "Hugo", "Lina", "Yassine", "Emma", "Maxime", "Nawel", "Romain", "Chloé",
    "Antoine", "Samira", "Bastien", "Lila", "Quentin", "Jade", "Yanis", "Camille", "Alexandre", "Hana",
    "Théo", "Myriam", "Enzo", "Salma", "Victor", "Zoé", "Ayoub", "Manon"
]

a = list(filter(lambda prenom: 'a' in prenom, eleves))
print(a)
list_sept_char = list(filter(lambda prenom : len(prenom)> 7, eleves))
print(list_sept_char)
list_last_position = list(filter(lambda prenom: prenom[len(prenom)-1] == 'd', eleves))
print(list_last_position)