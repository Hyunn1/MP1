principal = float(input("Enter the amount of money deposited: "))

rate = 0.04 
years = 3

for i in range(1, years + 1):
    
    amount = principal * (1 + rate)**i
    
    print(f"Year {i}: Savings Account Balance: ${amount:.2f}")
