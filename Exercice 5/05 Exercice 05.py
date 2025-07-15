mots = input("Entrez des mots séparés par des espaces : ").split()
voyelles = "aeiouyAEIOUY"  # Ajout des majuscules
total_voyelles = 0

for mot in mots:
    for lettre in mot.lower():  # Conversion en minuscule pour tout vérifier
        if lettre in voyelles:
            total_voyelles += 1

print(f"Nombre total de voyelles : {total_voyelles}")  # Correction f-string