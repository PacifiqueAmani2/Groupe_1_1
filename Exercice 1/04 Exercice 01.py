age = int(input("Age : "))
statut = input("Statut (étudiant/salarié/retraité) : ").lower()

# Correction de la structure if/else et des indentations
if age < 18:
    tarif = 5
elif 18 <= age <= 25:
    if statut == "étudiant":
        tarif = 6
    elif statut == "salarié":
        tarif = 8
    else:
        tarif = 10
else:  # age > 25
    if statut == "retraité":
        tarif = 7
    else:
        tarif = 10

print(f"Votre tarif est de {tarif} €.")