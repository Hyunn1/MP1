number = int(input("Enter four-digit integer: "))


sum_digits = sum(int(digit) for digit in str(number))


print(f"Sum of the four-digit integer ({number}): is {sum_digits}")