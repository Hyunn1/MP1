kpa = float(input("Enter pressure in kilopascals (kPa): "))

psi = kpa * 0.145038
mmhg = kpa * 7.50062
atm = kpa * 0.00986923

print(f"Pounds per square inch: {psi:.2f} PSI")
print(f"Millimeters of mercury: {mmhg:.2f} mmHg")
print(f"Atmospheres:            {atm:.4f} atm")