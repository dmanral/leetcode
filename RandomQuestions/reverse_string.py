# Given a string reverse it.

# Long way
def rev_str_long(something):
    temp = []
    temp_2 = []
    reversed = ""
    for char in something:
        temp.append(char)
    for i in range(len(temp), 0, -1):
        temp_2.append(temp[i-1])
    for chars in temp_2:
        reversed += chars
    return reversed

# print(rev_str_long('something'))

# Shortish-long way
def rev_str_shLong(something):
    reversed = ""
    for i in range(len(something), 0, -1):
        reversed += something[i-1]
    return reversed
print(rev_str_shLong('something'))

# Short way
def rev_str_short(something):
    return something[::-1]

# print(rev_str_short('lame ass'))
