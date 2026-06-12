#korting_calculator.py-gemaakt door Mishal_Ali

"""print("="*45)
print("korting checker-PrimaBouwBV")
print("="*45)

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
print("=" * 45)"""

"""print("="*45)
print(" veiligheids_assistent primaBouw BV")
print("="*45)
wind_kmh = float(input("wat is de actuele windsnelheid op de werp(km/u)?"))
if wind_kmh > 60:
    print("critieke gevaar: stoppen met alle werkzaamheden!Evacueer de stellingen")
elif wind_kmh > 30:
    netten = input("zijn de verplichte veligheids netten gemonteerd?(ja/nee): ")
    if netten.lower() == "ja":
        print("WAARSCHUWING: werken toegestaan, maar wees alert op rukwinden. ")
    else:
        print("GEVAAR: werken op hoogte VERBODEN zonder gemonteerde netten!")
else:
    regen = input("is er sprake van hevige regen op ijzel?(ja/ne)")
    if regen.lower() == "ja":
        print("WAARSCHUWING: risico op gladheid. Werken toegestaan met Antislip_schoeisel.")
    else:
        print(" VEILIG: Normale werkomstandigheden op de stellingen.")"""
    
print("\n--- EXTRA CONTROLE TORENKRAAN ---")
kraan_hoogte = float(input("Hoe hoog staat de kraanmast (in meters)? "))
wind_kmh = float(input("Hoe hars is het waait?"))
# Combineren met 'and' en 'or'
if wind_kmh > 45 and kraan_hoogte > 20:
    print(" KRAAN STATUS: Bediening VERBODEN wegens hefboomwind op grote hoogte.")
elif wind_kmh > 55 or kraan_hoogte > 40:
    print(" KRAAN STATUS: Alleen bediening door gecertificeerde masters. Wees uiterst voorzichtig.")
else:
    print(" KRAAN STATUS: Werking binnen de normale veiligheidsmarges.")



        