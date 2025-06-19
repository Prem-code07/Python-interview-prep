x=input("Enter a sterin :").lower()
a=['a','e','i','o','u']
s=0
for char in x:
    if char in a:
        s+=1
print(f"Total vowels are {s} .")
