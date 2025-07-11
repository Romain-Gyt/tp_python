import psycopg2


conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="wayallenmam",
    dbname="pingouins_db"
)

cursor = conn.cursor()


cursor.execute("SELECT COUNT(*) FROM pingouins")
print("Nombre total de pingouins :", cursor.fetchone()[0])


cursor.execute("SELECT espece, COUNT(*) FROM pingouins GROUP BY espece")
print("Individus par espèce :")
for row in cursor.fetchall():
    print(row)


cursor.execute("SELECT COUNT(DISTINCT espece) FROM pingouins")
print("Nombre d'espèces :", cursor.fetchone()[0])


cursor.execute("SELECT ile, COUNT(*) FROM pingouins GROUP BY ile")
print("Individus par île :")
for row in cursor.fetchall():
    print(row)


cursor.execute("SELECT COUNT(DISTINCT ile) FROM pingouins")
print("Nombre d'îles :", cursor.fetchone()[0])


cursor.execute("SELECT AVG(longueur_bec) FROM pingouins")
print("Longueur moyenne des becs :", cursor.fetchone()[0])


cursor.execute("SELECT MAX(profondeur_bec) FROM pingouins")
print("Profondeur maximale du bec :", cursor.fetchone()[0])


cursor.execute("SELECT sex, COUNT(*) FROM pingouins GROUP BY sex")
print("Individus par sexe :")
for row in cursor.fetchall():
    print(row)


cursor.execute("SELECT MAX(annee_naissance) FROM pingouins")
annee_jeune = cursor.fetchone()[0]
print("Année du plus jeune :", annee_jeune)


cursor.execute("SELECT MIN(annee_naissance) FROM pingouins")
annee_vieux = cursor.fetchone()[0]
print("Année du plus vieux :", annee_vieux)


cursor.close()
conn.close()
