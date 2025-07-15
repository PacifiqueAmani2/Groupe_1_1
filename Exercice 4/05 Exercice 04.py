# Génération des carrés
carres = [i**2 for i in range(1, 21)]  # Correction : 'i' -> 1

# Filtrage
carres_filtres = [x for x in carres if x > 100]

print("Tous les carrés :", carres)
print("\nCarrés > 100 :", carres_filtres)