a=str(int(input("Enter a number : ")))
if a==a[::-1]:
    print(f"{a} is Pallinrom.")
else:
    print(f"{a} is not a pallindrom.")