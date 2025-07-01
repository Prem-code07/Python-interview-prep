def find_difference(s, t):
    return chr(sum(map(ord, t)) - sum(map(ord, s)))
s = input("Enter a string : ")
t = input("Enter a string : ")
print(find_difference(s, t))
