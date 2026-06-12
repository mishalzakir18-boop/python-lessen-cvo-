# geintegreerd_menu.py – gemaakt door [jouw naam]

while True:
    print("\n" + "=" * 45)
    print(" HOOFDMENU ERPM-SYSTEEM PRIMABOUW")
    print("=" * 45)
    print("1: BTW-Calculator (Les 3)")
    print("2: Kortingscalculator (Les 4)")
    print("3: Werf- & Stellingveiligheid (Les 4)")
    print("4: Applicatie afsluiten")
    print("=" * 45)


    keuze = input("Maak uw keuze (1-4): ")

    if keuze == "1":
        print("\n--- [OPSTARTEN BTW-CALCULATOR] ---")

        bedrag = float(input("Geef het bedrag exclusief BTW in: €"))
        btw_tarief = float(input("Geef het BTW-tarief in (%): "))

        btw_bedrag = bedrag * (btw_tarief / 100)
        totaal = bedrag + btw_bedrag

        print(f"Bedrag exclusief BTW: €{bedrag:.2f}")
        print(f"BTW-bedrag: €{btw_bedrag:.2f}")
        print(f"Bedrag inclusief BTW: €{totaal:.2f}")

    elif keuze == "2":
        print("\n--- [OPSTARTEN KORTINGSCALCULATOR] ---")

        totaalbedrag = float(input("Geef het orderbedrag in: €"))

        if totaalbedrag >= 2500:
            korting_pct = 15
        elif totaalbedrag >= 1000:
            korting_pct = 10
        elif totaalbedrag >= 500:
            korting_pct = 5
        else:
            korting_pct = 0

        kortingsbedrag = totaalbedrag * (korting_pct / 100)
        eindbedrag = totaalbedrag - kortingsbedrag

        print("-" * 45)
        print(f"Bruto orderbedrag : €{totaalbedrag:.2f}")
        print(f"Kortingspercentage: {korting_pct}%")
        print(f"Kortingsbedrag    : €{kortingsbedrag:.2f}")
        print(f"Netto te betalen  : €{eindbedrag:.2f}")
        print("=" * 45)

    elif keuze == "3":
        print("\n--- [OPSTARTEN WERF-VEILIGHEID] ---")

        wind_kmh = float(input("Geef de windsnelheid in (km/u): "))

        if wind_kmh > 60:
            print(" Veiligheidsstatus: Werken verboden!")
        elif wind_kmh > 40:
            print(" Veiligheidsstatus: Extra voorzichtigheid vereist!")
        else:
            print(" Veiligheidsstatus: Werken toegestaan.")

        print("\n--- EXTRA CONTROLE TORENKRAAN ---")
        kraan_hoogte = float(input("Hoe hoog staat de kraanmast (in meters)? "))

        if wind_kmh > 45 and kraan_hoogte > 20:
            print(" KRAAN STATUS: Bediening VERBODEN wegens hefboomwind op grote hoogte.")
        elif wind_kmh > 55 or kraan_hoogte > 40:
            print("KRAAN STATUS: Alleen bediening door gecertificeerde masters. Wees uiterst voorzichtig.")
        else:
            print(" KRAAN STATUS: Werking binnen de normale veiligheidsmarges.")

    elif keuze == "4":
        print("\nBedankt voor het gebruiken van het PrimaBouw systeem. Tot ziens!")
        break

    else:
        print("❌ Ongeldige keuze! Voer een cijfer van 1 tot en met 4 in.")