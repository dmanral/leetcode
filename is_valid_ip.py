# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89

# Examples of invalid inputs:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

# Notes:

# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

def is_valid_ip(string):
    inputList = list(string.split("."))
    length = len(inputList)

    # Initial check.
    if length != 4:
        return False

    numbList = [str(item) for item in range(0,256)]

    # Leading 0s and not in numb list.
    for numb in inputList:
        if len(numb) > 1:
            if numb.startswith('0'):
                return False
        if numb not in numbList:
            return False
    
    return True

print(is_valid_ip('1.2.3.4'))           # True
print(is_valid_ip('123.45.67.89'))      # True
print(is_valid_ip('0.34.82.53'))        # True
print(is_valid_ip('0.0.0.0'))           # True
print(is_valid_ip('127.1.1.0'))         # True

print(is_valid_ip('1.2.3'))             # False
print(is_valid_ip('1.2.3.4.5'))         # False
print(is_valid_ip('123.456.78.90'))     # False
print(is_valid_ip('123.045.067.089'))   # False
