def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(f"GCD is: {gcd(12, 18)}")
