a = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]  # Each tuple should use comma, not colon.
b, c = zip(*a)
print(b)
print(c)