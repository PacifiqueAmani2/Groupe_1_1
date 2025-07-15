entree = input("Entrez des nombres séparés par des espaces : ")
liste = [int(x) for x in entree.split()]  # Correction : parenthèse fermante

somme_pairs = sum(x for x in liste if x % 2 == 0)  # Version optimisée

print(f"Somme des nombres pairs : {somme_pairs}")