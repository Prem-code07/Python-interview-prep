# a=input("Enter a paranthesis for check it is avalid or not  : ")
# b=['[]','{}','()']
# if a in b:
#     print(f"{a} is a valid paranthesis.")
# else:
#     print(f"{a} is not a valid parenthsis.")
def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

a = input("Enter a parenthesis string to check if it is valid or not: ")

if is_valid_parentheses(a):
    print(f"{a} is a valid parenthesis.")
else:
    print(f"{a} is not a valid parenthesis.")
