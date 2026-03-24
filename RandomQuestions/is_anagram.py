def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {} 

    for stuff in s:
        if stuff in s_dict:
            s_dict[stuff] += 1
        else:
            s_dict[stuff] = 1

    for stuff in t:
        if stuff in t_dict:
            t_dict[stuff] += 1
        else:
            t_dict[stuff] = 1

    if s_dict == t_dict:
        return True
    else:
        return False

print(isAnagram("anargam", "nagaram"))
print(isAnagram("rat", "car"))
# print(isAnagram("anargam", "nagaram"))
# print(isAnagram("anargam", "nagaram"))