def pallindrome (n):
    if n==n[::-1]:
        print("This is palindrom string .")
    else:
        print("This is not a pallindrom string.")
a=input("Enter a numbber : ")
pallindrome(a)