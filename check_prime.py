n=int(input("Enter a number : "))
if n <=1:
    print(f"{n} number can't get prime number.") 
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")