def pangram(a):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(a.lower()))
text = "The quick brown fox jumps over the lazy dog"
print(pangram(text))
