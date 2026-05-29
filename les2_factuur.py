klant = input("Naam van de klant: ")
aantal = int(input("Aantal producten: "))

if aantal < 0:
    print("FOUT: aantal producten mag niet negatief zijn.")
else:
    prijs = float(input("Prijs per stuk: € "))
    btw_percentage = float(input("BTW-percentage (6, 12 of 21): "))

    
    subtotaal = aantal * prijs
    btw = subtotaal * (btw_percentage / 100)
    totaal = subtotaal + btw

    
    print("===============================")
    print("Factuur voor:", klant)
    print("Aantal producten:", aantal)
    print(f"Prijs per stuk:  € {prijs:.2f}")
    print("--------------------------------")
    print(f"Subtotaal:       € {subtotaal:.2f}")
    print(f"BTW ({btw_percentage}%):      € {btw:.2f}")
    print(f"TOTAAL:          € {totaal:.2f}")
    print("===============================")