day_old_loaves = int(input("Enter the number of day old loaves: ")) 
 
regular_price = 3.49 
discount = 60 
 
regular_total = day_old_loaves * regular_price 
discount_amount = regular_total * (discount / 100) 
final_price = regular_total - discount_amount 
 
print(f"Regular Price:	${regular_total:<6.2f}") 
print(f"Discount (60%):	${discount_amount:<6.2f}") 
print(f"Total Price:	${final_price:<6.2f}")