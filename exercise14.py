INCHES_PER_FOOT = 12
CM_PER_INCH = 2.54

feet = int(input("Enter number of feet: "))
inches = int(input("Enter number of inches: "))

total_inches = (feet * INCHES_PER_FOOT) + inches
centimeters = total_inches * CM_PER_INCH

print(f"The equivalent height is {centimeters:.2f} cm.")
