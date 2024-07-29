# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 

# Example 1:

# Input: s = "42"

# Output: 42

# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:

# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.

 

# Constraints:

# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Edge Case: If the string is empty, return 0.
        if not s:
            return 0

        # Remove whitespace from the string.
        s = s.strip()

        # If string is empty after removing whitespace, return 0.
        if not s:
            return 0
        
        # If there is a sign in the string, store  it in a variable.
        sign = 1
        if s[0] == '-':
            if len(s) > 1 and s[1].isdigit():
                sign = -1
                s = s[1:]
            else:
                return 0
        elif s[0] == '+':
            if len(s) > 1 and s[1].isdigit():
                s = s[1:]
            else:
                return 0
        elif s[0] == '.':
            return 0
        else:
            s = s[0:]
        
        # Remove leading zeros only if the 1st char is a zero and the 2nd char is a digit.
        # Else, return 0.
        if s[0] == '0':
            s = s[1:]
        elif s[0] == '0' and not s[1].isdigit():
            return 0

        # If 1st char is not a digit, return 0.
        if not s[0].isdigit():
            return 0
        
        # Digits in list.
        numblist = []
        for chars in s:
            if chars.isdigit():
                numblist.append(chars)
            else:
                break
        # Join the digits in the list to create a new number string.
        result = ''.join(numblist)
        # Convert the number string to an integer and multiply by sign.
        result = int(result) * sign

        # Rounding the integer to remain in the 32-bit signed integer range.
        # A signed integer is a 32-bit datum that encodes an integer in the range [-2147483648 to 2147483647].
        if result < -2**31:
            result = -2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1
        
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.myAtoi("42")
    print(result)
    result2 = solution.myAtoi("-042")
    print(result2)
    result3 = solution.myAtoi("1337c0d3")
    print(result3)
    result4 = solution.myAtoi("0-1")
    print(result4)
    result5 = solution.myAtoi("words and 987")
    print(result5)
    result6 = solution.myAtoi("-91283472332")
    print(result6)
    result7 = solution.myAtoi("91283472332")
    print(result7)
    result8 = solution.myAtoi("-")
    print(result8)