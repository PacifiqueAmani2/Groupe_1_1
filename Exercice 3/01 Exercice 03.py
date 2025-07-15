# === Saisie de l'utilisateur ===
heures = int(input("Nombre d'heures : "))
minutes = int(input("Nombre de minutes : "))
secondes = int(input("Nombre de secondes : "))

# === Conversion en secondes ===
total_secondes = heures * 3600 + minutes * 60 + secondes

# === Affichage du résultat ===
print(f"Durée totale : {total_secondes} secondes.")
