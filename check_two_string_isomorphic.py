def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping_s_t = {}
    mapping_t_s = {}

    for ch1, ch2 in zip(s, t):
        if ch1 in mapping_s_t:
            if mapping_s_t[ch1] != ch2:
                return False
        else:
            mapping_s_t[ch1] = ch2

        if ch2 in mapping_t_s:
            if mapping_t_s[ch2] != ch1:
                return False
        else:
            mapping_t_s[ch2] = ch1

    return True
print(is_isomorphic("egg", "add"))    
print(is_isomorphic("foo", "bar"))    
print(is_isomorphic("paper", "title"))
