# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


from typing import List

# My solution is horrible when the height is massive.
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # Container seems to be more or less a rectangle so we can calculate the area of the rectangle by multiplying the width(height) and length(difference in indices) of the rectangle.
#         # The height will always be the minimum of the two heights of the vertical lines.
#         # The width will be the difference between the two indices of the vertical lines.
#         # We can use hashtables to store the area of each rectangle.
#         # We can then return the maximum area of the rectangle.
#         if len(height) == 2:
#             for item in height:
#                 if item == 0:
#                     return 0
        
#         area = 0
#         all_pairs = [(i, j+i+1, a, b) for i, a in enumerate(height) for j, b in enumerate(height[i +1:])]   # i and j are indicies for a and b respectively.
#         # print(all_pairs)
    
#         # key value pair according to distance from each other
#         distance_pairs = {}
#         for i, j, pair1, pair2 in all_pairs:
#             distance = abs(i-j)
#             if distance not in distance_pairs:
#                 distance_pairs[distance] = [[pair1, pair2]]
#             else:
#                 distance_pairs[distance].append([pair1, pair2])
            
#         # print(distance_pairs)

#         for key, value_list in distance_pairs.items():
#             for value in value_list:
#                 temp_area = key * min(value)
#                 if temp_area > area:
#                     area = temp_area
#         return area

# This is chatgpt's solution and its a lot better.
# This is called he two-pointer technique.
# 1. Start with the two pointers, one at the beginning and one at the end of the array.
# 2. Calculate the area between these two points and keep track of the maximum area seen so far,
# 3. Move the pointer with the smaller height towards the other pointer.
# This has a time complexity of O(n) and a space complexity of O(1).
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0                                    # Pointer at the beginning of the array.
        right = len(height) - 1                     # Pointer at the end of the array.

        while left < right:                         # While there are elements to compare.
            # Calculate the area
            h = min(height[left], height[right])    # Height of the rectangle.
            w = right - left                        # Width of the rectangle.
            area = h * w                            # Area of the rectangle.

            # Update the maximum area if necessary
            max_area = max(max_area, area)          # If the new area is greater than the max area, update the max area.

            # Move the poiners
            if height[left] < height[right]:        # If the height at the left pointer is less than the height at the right pointer, move the left pointer to the right.
                left += 1
            else:                                   # If the height at the left pointer is greater than or equal to the height at the right pointer, move the right pointer to the left.
                right -= 1
        
        return max_area

if __name__ == "__main__":
    solution = Solution()
    result = solution.maxArea([1,8,6,2,5,4,8,3,7])
    print(result)
    result1 = solution.maxArea([1,1])
    print(result1)
    result2 = solution.maxArea([4,3,2,1,4])
    print(result2)
    result3 = solution.maxArea([0,2])
    print(result3)
    result4 = solution.maxArea([1,0,0,0,0,0,0,2,2])
    print(result4)
    result5 = solution.maxArea([2,3,4,5,18,17,6])
    print(result5)