a=int(input("ENter a number : "))
b=[1,2,2,1]
print(f"Before remove elemnt the leangth is {len(b)}.")
for i in b:
    if i ==a:
        b.remove(a)
print(f"After remove elemnt the leangth is {len(b)}.")