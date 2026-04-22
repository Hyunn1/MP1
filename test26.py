weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print(f"Your Body Mass Index (BMI) is {bmi:.2f}")