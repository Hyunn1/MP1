ft = float(input("Enter Measurement in Feet: "))


inches = ft * 12
yards = ft / 3
miles = ft / 5280


print(f"Feet to Inches: {inches:.2f} in")
print(f"Feet to Yards: {yards:.2f} yd")
print(f"Feet to Miles: {miles:.5f} mi")