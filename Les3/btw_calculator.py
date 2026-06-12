# btw_calculator.py – gemaakt door [Mishal]

print("BTW_calculator - Primabouw BV")
print("=" * 45)

gebruiker = input("Jouw naam: ")
print(f"Welkom, {gebruiker}!")
print("=" * 45)

bedrag_str = input("Voer het bedrag in (excl. BTW, in €): ")
bedrag = float(bedrag_str)

tarief_str = input("Welk BTW-tarief? (6, 12 of 21): ") 
tarief = int(tarief_str)

btw_bedrag = bedrag * (tarief / 100)
totaal = bedrag + btw_bedrag

print("-" * 45)
print(f"Bedrag excl. BTW : €{bedrag:.2f}")
print(f"BTW ({tarief}%)        : €{btw_bedrag:.2f}")
print(f"Totaal incl. BTW : €{totaal:.2f}")
print("=" * 45)

btw_pct_totaal = (btw_bedrag/totaal)*100
print(f"BTW als % van totaal: {btw_pct_totaal:.1f}%")

nog_een = input("\nWil je nog een berekening? (ja/nee): ")

if nog_een.lower() == "ja":
    print("Start het script opnieuw om een nieuwe berekening te doen.")
else:
    print("Tot de volgende keer, " + gebruiker + "!")



 