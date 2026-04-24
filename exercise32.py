num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)
middle = (num1 + num2 + num3) - smallest - largest

print(f"Sorted order: {smallest}, {middle}, {largest}")
