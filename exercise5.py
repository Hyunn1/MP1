less_than_liter = int(input("Enter the number of containers (1 liter or less): "))
more_than_liter = int(input("Enter the number of containers (more than 1 liter): "))

refund_amount = (less_than_liter * 0.10) + (more_than_liter * 0.25)

print(f"Refund amount: ${refund_amount:.2f}")10
