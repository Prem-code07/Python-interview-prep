str1=input("Enter a string :")
str2=input("Enter a string :")
str1=str1.replace(" ","").lower()
str2=str2.replace(" ","").lower()
if sorted(str1)==sorted(str2):
    print("Angrum")
else:
    print("ngrum")