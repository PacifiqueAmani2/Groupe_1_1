anciennete = int(input("Années d'ancienneté : "))
note = int(input("Note de performance (1-5) : "))

# Vérification des entrées
if note < 1 or note > 5:
    print("Erreur : la note doit être entre 1 et 5")
    exit()

# Calcul de la prime
if anciennete >= 5:
    prime = 2000 if note >= 4 else 1000
else:
    prime = 500 if note >= 4 else 0

print(f"Prime attribuée : {prime} €")