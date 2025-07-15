entree = input("Entrez des elements : ")
liste = entree.split()

liste_inverse = []

for i in range(len(liste) - 1, -1, -1):
    liste_inverse.append(liste[i])

print(f"liste inverse = {liste_inverse}")