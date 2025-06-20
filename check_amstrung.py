n = int(input("Enter a number: "))
n_str=str(n)
n_digits = len(n_str)
sum_of_powers = sum(int(digit) ** n_digits for digit in n_str)
if n == sum_of_powers:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
