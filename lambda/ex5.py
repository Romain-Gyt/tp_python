from collections import defaultdict
from functools import reduce

eleves = [
    ("Karim Benali", 11),
    ("Ines Dubois", 9),
    ("Adrien Lefèvre", 10),
    ("Sofia Haddad", 9),
    ("Mehdi Bensalem", 19),
    ("Clara Moreau", 6),
    ("Julien Marchand", 18),
    ("Amira Zeroual", 5),
    ("Lucas Petit", 20),
    ("Sarah Khelifi", 15),
    ("Nicolas Durand", 19),
    ("Leïla Bouzid", 6),
    ("Thomas Lambert", 11),
    ("Amina Taleb", 8),
    ("Hugo Fontaine", 18),
    ("Lina Merabet", 4),
    ("Yassine El Moudden", 4),
    ("Emma Lemoine", 12),
    ("Maxime Garcia", 10),
    ("Nawel Aït Ali", 14),
    ("Romain Girard", 3),
    ("Chloé Bernard", 19),
    ("Antoine Masson", 14),
    ("Samira Bekkali", 8),
    ("Bastien Roche", 17),
    ("Lila Benyahia", 17),
    ("Quentin Noël", 12),
    ("Jade Amrani", 13),
    ("Yanis Saidi", 6),
    ("Camille Robert", 19),
    ("Alexandre Fabre", 11),
    ("Hana Moumen", 4),
    ("Théo Muller", 7),
    ("Myriam Djemai", 13),
    ("Enzo Caron", 5),
    ("Salma Charef", 3),
    ("Victor Perrin", 19),
    ("Zoé Rahmani", 15),
    ("Ayoub Sebbar", 10),
    ("Manon Tessier", 1)
]

# utilise cette liste pour créer un dictionnaire où la clé est la note et la valeur la liste des "prénom nom" ayant eu cette note
# exemple {..., 19 : ["Victor Perrin", "Camille Robert"]



eleves_par_note =  dict()

for nom, note in eleves:
    eleves_par_note[note]=nom


for note in sorted(eleves_par_note):
    print(f"{note} : {eleves_par_note[note]}")
