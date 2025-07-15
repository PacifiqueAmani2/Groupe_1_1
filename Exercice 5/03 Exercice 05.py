# Vérification robuste de mot de passe
mdp = input("Entrez un mot de passe : ")

longueur_ok = len(mdp) >= 8
contient_chiffre = any(c.isdigit() for c in mdp)
contient_majuscule = any(c.isupper() for c in mdp)
contient_minuscule = any(c.islower() for c in mdp)
contient_special = any(not c.isalnum() for c in mdp)

if longueur_ok and contient_chiffre and contient_majuscule and contient_minuscule and contient_special:
    print("✅ Mot de passe sécurisé")
elif longueur_ok and contient_chiffre and contient_majuscule:
    print("⚠️ Mot de passe valide mais peu sécurisé (ajoutez des caractères spéciaux)")
else:
    print("❌ Mot de passe invalide")
    print("Critères requis :")
    print("- 8 caractères minimum")
    print("- Au moins un chiffre")
    print("- Majuscule et minuscule")
    print("- Caractère spécial recommandé")