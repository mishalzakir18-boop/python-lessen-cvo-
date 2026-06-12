# les2_oefC.py


getal1 = int(input("Voer het eerste gehele getal in: "))
getal2 = int(input("Voer het tweede gehele getal in: "))

som = getal1 + getal2
verschil = getal1 - getal2 
product = getal1 * getal2
deling = getal1 / getal2


print("Som:", som)
print("Verschil:", verschil)
print("Product:", product)
print("Deling:", deling)


getal1 = int(input("Voer het eerste gehele getal in: "))
getal2 = int(input("Voer het tweede gehele getal in: "))


som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2
deling = getal1 / getal2
kwadraat = getal1 ** 2


if getal1 % 2 == 0:
    soort = "even"
else:
    soort = "oneven"


print("Som:", som)
print("Verschil:", verschil)
print("Product:", product)
print("Deling:", deling)
print("Kwadraat van het eerste getal:", kwadraat)
print("Het eerste getal is:", soort)