# Takes an integer for the size of the triangle.
def twoTriangles(size):
    i = 1
    while (i <= size):
        print("*" * i)
        i += 1
    
    j = 0
    while (j < size):
        print("*" * (size-j))
        size -= 1

# Better and cleaner version.
def twoTriangles2(size):
    lines = []
    for i in range(1, size + 1):
        lines.append("*" * i)

    for j in range(size, 0, -1):
        lines.append("*" * j)
    return "\n".join(lines)

# print(twoTriangles(7))
print(twoTriangles2(7))