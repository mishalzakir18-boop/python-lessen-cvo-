#U1: Klantsegmentatie

totaalbedrag = float(input("Geef het orderbedrag in: €"))
klanttype = input("Geef klanttype (Standaard, Zilver, Goud): ")

if totaalbedrag >= 2500:
    korting_pct = 15
elif totaalbedrag >= 1000: 
    korting_pct = 10
elif totaalbedrag >= 500:
    korting_pct = 5
else:
    korting_pct = 0

# extra korting op basis van klanttype
if klanttype == "Goud":
    korting_pct += 5
elif klanttype == "Zilver":
    korting_pct += 2

kortingsbedrag = totaalbedrag * (korting_pct / 100)
eindbedrag = totaalbedrag - kortingsbedrag

print(f"Korting totaal: {korting_pct}%")
print(f"Eindbedrag: €{eindbedrag:.2f}")

#U2: Input Validatie met isdigit()
bedrag_input = input("Geef een bedrag in: ")

if bedrag_input.isdigit():
    bedrag = float(bedrag_input)
else:
    print(" Ongeldige invoer, standaardwaarde 0 gebruikt.")
    bedrag = 0

#U3: Uitgebreide Werfevaluatie
print("\n--- OFFERTESYSTEEM ---")

winst = float(input("Geschatte winst (€): "))
personeel = int(input("Beschikbaar personeel: "))
risico = input("Risicofactor (Laag, Medium, Hoog): ")

if winst < 5000 and risico == "Hoog":
    print(" GEWEIGERD: te hoog risico bij lage winst.")

elif personeel < 3:
    print("⏸ ON HOLD: onvoldoende personeel beschikbaar.")

else:
    print(" GOEDGEKEURD: project kan starten.")