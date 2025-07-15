print("\nMenu du restaurant :")
print("1. Viande")
print("2. Poisson")
print("3. Végétarien\n")

plat = input("Choisissez un plat (viande/poisson/végétarien) : ").lower()

if plat == "viande":
    print("\nOptions de cuisson :")
    print("- Saignant")
    print("- À point")
    print("- Bien cuit")
    cuisson = input("\nVotre choix de cuisson : ").lower()
    print(f"\nCommande : Viande {cuisson}")

elif plat == "poisson":
    print("\nSauces disponibles :")
    print("- Citron")
    print("- Beurre blanc")
    sauce = input("\nVotre choix de sauce : ").lower()
    print(f"\nCommande : Poisson sauce {sauce}")

elif plat == "végétarien":
    print("\nOptions végétariennes :")
    print("- Salade composée")
    print("- Pâtes primavera")
    choix = input("\nVotre choix : ").lower()
    print(f"\nCommande : {choix.capitalize()}")

else:
    print("\nErreur : choix non disponible")
    print("Veuillez choisir entre viande, poisson ou végétarien")