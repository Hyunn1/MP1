length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

area = length * width

acre = area / 43560

print(f"The area of the field is {acre:.2f} acres" )