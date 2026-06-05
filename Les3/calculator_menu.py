while True:
    print("\n1) BTW berekenen")
    print("2) Temperatuur omrekenen")
    print("3) Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        bedrag = float(input("Bedrag: "))
        btw = bedrag * 0.21
        print("BTW:", btw)
        print("Totaal:", bedrag + btw)

    elif keuze == "2":
        c = float(input("Celsius: "))
        print("Fahrenheit:", c * 1.8 + 32)

    elif keuze == "3":
        print("Stop")
        break

    else:
        print("Ongeldige keuze")