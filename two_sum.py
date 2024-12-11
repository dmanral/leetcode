# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not
# use the same element twice.
#
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum_brute(list, target):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return([i,j])

print(twoSum_brute([2,15,11,7], 9))
print(twoSum_brute([3,2,4], 6))
print(twoSum_brute([3,3], 6))

def twoSum(list, target):
    # Dictionary
    D = {}
    # Enumerate gives you both index and value.
    for i,num in enumerate(list):
        complement = target - num
        if complement in D.keys():
            return([D[complement], i])
        D[num] = i

print(twoSum([2,15,11,7], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
