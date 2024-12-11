# Description
# Create a function that takes one argument: a number (baseWidth). 
# Your function should return a string that shows a triangle, where the base 
# of the triangle has baseWidth characters.

# Input
# baseWidth How wide the base of the triangle is

# Type: integer

# Constraint: >= 0

# Examples
# baseWidth = 5;

#   *
#  ***
# *****
# baseWidth = 6;

#   **
#  ****
# ******

def pyramid(baseWidth):
    counter = 1
    # Number of spaces
    space = baseWidth - 1

    # number of rows
    for i in range(0, baseWidth):
        if baseWidth % 2 == 0:
            print("*" * baseWidth)
            baseWidth -= 2
            print("\r")
        else:
            print("*" * baseWidth)
            baseWidth -= 1
            print("\r")


print(pyramid(5))
print(pyramid(6))