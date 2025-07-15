def convertir(usd):
    eur = usd * 0.93
    cfa = usd * 610
    gbp = usd * 0.79
    return eur, cfa, gbp

montant = float(input("Montant en USD : "))
eur, cfa, gbp = convertir(montant)
print(f"{montant} USD = {eur:.2f} EUR, {cfa:.2f} CFA, {gbp:.2f} GBP")