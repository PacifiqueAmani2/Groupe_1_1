nombre = int(input("Entrez un nombre pour sa table de multiplication : "))

print(f"\n=== Table de {nombre} ===")
for i in range(1, 13):  # Correction : 'i' -> 1
    resultat = nombre * i
    print(f"{nombre} × {i:2d} = {resultat:3d}")  # Formatage amélioré