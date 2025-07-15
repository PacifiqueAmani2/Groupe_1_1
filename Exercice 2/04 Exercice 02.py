role = input("Rôle (employé/visiteur/sécurité) : ").lower()

if role == "employé":
    badge = input("Badge valide ? (oui/non) : ").lower()
    if badge == "oui":
        print("Accès autorisé. Bonne journée !")
    else:
        print("Accès refusé : badge invalide ou expiré.")
        print("Veuillez contacter le service RH.")
elif role == "visiteur":
    rdv = input("Avez-vous un rendez-vous ? (oui/non) : ").lower()
    if rdv == "oui":
        personne = input("Nom de la personne visitée : ")
        print(f"Accès autorisé. Direction le bureau de {personne}.")
    else:
        print("Accès refusé : rendez-vous requis.")
        print("Merci de prendre contact par téléphone.")
elif role == "sécurité":
    print("Accès prioritaire autorisé.")
    print("Bonne patrouille !")
else:
    print("Accès refusé : rôle non reconnu.")
    print("Les rôles valides sont : employé, visiteur, sécurité")