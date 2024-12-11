# Complete the solution so that the function will break up camel casing, using a space between words.

# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
import re
def breakCamelCase(s):
    stringList = [item for item in re.findall('[a-zA-Z][^A-Z]*', s)]
    return ' '.join(stringList)

print(breakCamelCase('camelCasing'))
print(breakCamelCase('identifier'))
print(breakCamelCase(''))
