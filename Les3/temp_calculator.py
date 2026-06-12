# temp_calculator.py – gemaakt door [Mishal]
print("=" * 40)
print("  Temperatuuromrekening F → C")
print("=" * 40)

print("=" * 40)
print("  Temperatuuromrekening F → C")
print("=" * 40)

fahrenheit_input = float(input("Geef een temperatuur in °F: "))
celsius_output = (fahrenheit_input - 32) * 5 / 9

print(f"{fahrenheit_input:.1f} °F = {celsius_output:.1f} °C")


fahrenheit_value = float(input("Geef een temperatuur in °F: "))
celsius_value = (fahrenheit_value - 32) * 5 / 9

print(f"{fahrenheit_value:.1f} °F = {celsius_value:.1f} °C")

celsius_input = float(input("Geef een temperatuur in °C: "))
fahrenheit_output = (celsius_input * 9 / 5) + 32
print(f"{celsius_input:.1f} °C = {fahrenheit_output:.1f} °F")
