# === Demande d'informations à l'utilisateur ===
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

# === Calcul approximatif du nombre de jours vécus ===
jours_vécus = age * 365

# === Affichage du profil utilisateur ===
print("\n=== PROFIL UTILISATEUR ===")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans ({jours_vécus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")
