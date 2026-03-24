# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1 or numRows is greater than the length of the string, return the string as it is.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # List of empty strings with length equal to numRows.
        res = [''] * numRows
        # Index to keep track of the row number, step to keep track of the direction of the zigzag pattern.
        index, step = 0, 1

        for char in s:
            res[index] += char
            print(res)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()
    result = solution.convert("PAYPALISHIRING", 3)
    print(result)
    result2 = solution.convert("PAYPALISHIRING", 4)
    print(result2)
