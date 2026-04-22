TAX_RATE = 0.05
TIP_RATE = 0.18

cost = float(input("Enter the cost of the meal: "))

tax_amount = cost * TAX_RATE
tip_amount = cost * TIP_RATE
grand_total = cost + tax_amount + tip_amount

print(f"Tax amount:    ${tax_amount:.2f}")
print(f"Tip amount:    ${tip_amount:.2f}")
print(f"Grand total:   ${grand_total:.2f}")