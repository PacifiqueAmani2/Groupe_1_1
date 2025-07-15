# Analyse de température
temp = float(input("Température (°C) : "))

if temp >= 35:
    print("Alerte canicule ! Restez à l'ombre et hydratez-vous.")
elif temp >= 25:
    print("Température estivale. Protégez-vous du soleil.")
elif temp >= 15:
    print("Conditions climatiques idéales.")
elif temp >= 0:
    print("Température fraîche. Vêtements chauds recommandés.")
else:
    print("Froid glacial. Évitez les sorties prolongées.")