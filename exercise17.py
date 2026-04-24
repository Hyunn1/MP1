mass = float(input("Enter the mass of the water: "))
temp_change = float(input("Enter the temperature change: "))

specific_heat = 4.186 

heat_energy = mass * specific_heat * temp_change

print(f"Total energy required: {heat_energy:.2f} Joules")

joules_per_kwh = 3600000
kwh_used = heat_energy / joules_per_kwh

cost_in_cents = kwh_used * 8.9

print(f"The cost of heating the water is: {cost_in_cents:.2f} cents")
