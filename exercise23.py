import math


s = int(input("Enter length of a side (s): "))
n = int(input("Enter number of sides (n): "))
area = (n * s**2) /(4 * math.tan(math.pi / n))


print(f"Area of the Regular Polygon: {area:.2f}")