texte = input("Entrez une chaîne : ")
inverse = texte[::-1]  # Méthode Pythonique

# Version avec boucle (comme demandé)
inverse_boucle = ""
for char in texte:
    inverse_boucle = char + inverse_boucle

print(f"\nChaîne inversée (méthode slice): {inverse}")
print(f"Chaîne inversée (méthode boucle): {inverse_boucle}")