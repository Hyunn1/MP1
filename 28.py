import math

Ta = float(input("Enter air temperature (°C): "))
V = float(input("Enter wind speed (km/h): "))

if Ta <= 10 and V > 4.8:
    WCI = 13.12 + (0.6215 * Ta) - (11.37 * (V ** 0.16)) + (0.3965 * Ta * (V ** 0.16))
    print(f"Wind chill index: {round(WCI)}")
else:
    print("Wind chill index not valid for these values.")
    print("(Requires temp ≤ 10°C and wind > 4.8 km/h)")