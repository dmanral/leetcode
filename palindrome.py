# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:

# -2^31 <= x <= 2^31 - 1

# Follow up: Could you solve it without converting the integer to a string?

# Easiest solution would be to convernt integer to string.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        intToString = str(x)
        return intToString == intToString[::-1]
    
    def isPalindromeWithoutString(self, x: int) -> bool:
        # Negative numbers can never be palindromes.
        if x < 0:                                           # Using 121 as example, in this line its not less than 0, so skip.
            return False
        if x < 10:                                          # Using 121 as example, in this line its not less than 10, so skip.
            return True
        
        reversedNum = 0                                     # Intial value always 0, using 121 as example, in this line reversedNum is 0.
        originalNum = x                                     # Using 121 as example, in this line originalNum is 121 and always x.           
        while x > 0:                                        # Using 121 as example, in this line x is 121, so enter the loop.
            lastDigit = x % 10                              # Using 121 as example, in this line lastDigit is 1, because 121 % 10 is 1.
            reversedNum = reversedNum * 10 + lastDigit      # Using 121 as example, in this line reversedNum is 1, because 0 * 10 + 1 is 1.
            x = x // 10                                     # Using 121 as example, in this line x is 12, because 121 // 10 is 12.
        
        return originalNum == reversedNum                   # Using 121 as example, in this line originalNum is 121 and reversedNum is 121, so return True.
        
        
        

if __name__ == "__main__":
    solution = Solution()
    result = solution.isPalindrome(121)
    print(result)
    result = solution.isPalindrome(-121)
    print(result)
    result = solution.isPalindrome(10)
    print(result)
    result = solution.isPalindrome(9)
    print(result)

    result = solution.isPalindromeWithoutString(121)
    print(result)
    result = solution.isPalindromeWithoutString(-121)
    print(result)
    result = solution.isPalindromeWithoutString(10)
    print(result)
    result = solution.isPalindromeWithoutString(9)
    print(result)