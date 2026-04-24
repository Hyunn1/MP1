import math

r = float(input("Enter radius: "))

area = math.pi * r ** 2

volume = (4/3) * math.pi * r ** 3

print(f"Area of circle: {area:.2f}")
print(f"Volume of sphere: {volume:.2f}")