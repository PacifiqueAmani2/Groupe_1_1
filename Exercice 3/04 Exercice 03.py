fièvre = input("Avez-vous de la fièvre ? (oui/non) : ").lower()

if fièvre == "oui":
    douleurs = input("Avez-vous des douleurs ? (oui/non) : ").lower()
    if douleurs == "oui":
        print("Consultez un médecin rapidement.")
    else:
        print("Surveillez vos symptômes et reposez-vous.")
        print("Prenez votre température toutes les 4 heures.")
else:
    toux = input("Avez-vous une toux ? (oui/non) : ").lower()
    if toux == "oui":
        print("Repos conseillé avec hydratation abondante.")
        print("Si la toux persiste plus de 3 jours, consultez.")
    else:
        print("Votre état semble normal. Continuez à surveiller votre santé.")