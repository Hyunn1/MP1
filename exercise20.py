P = float(input("Enter pressure in Pascals: "))
V = float(input("Enter volume in liters: "))
Temp_celsius = float(input("Enter temperature in Celsius: "))

T = Temp_celsius + 273.15

R = 8.314

n = (P * V) / (R * T)

print(f"Amount of gas: {n:.2f} moles")

print("\nTest with SCUBA tank (12L, 20,000,000 Pa, 20°C):")
n_scuba = (20000000 * 12) / (8.314 * 293.15)
print(f"SCUBA tank contains: {n_scuba:.2f} moles")
