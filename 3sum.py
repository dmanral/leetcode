# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case
        if len(nums) == 3 and sum(nums) != 0:
            return []
        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]

        # Return all triplets that sum up to 0.
        triplets = []

        # Lets sort the list.
        nums.sort()

        # Lets use combinations to get all possible triplets.
        triplets = list(combinations(nums, 3))
        for triplet in triplets:
            if sum(triplet) != 0:
                triplets.remove(triplet)

        # Loop through the list and find all triplets that sum up to 0.
        # This is horribly inefficient O(n^3) solution.
        # for i in range(0, len(nums)-2):
        #     for j in range(i + 1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = []
        #                 temp.append(nums[i])
        #                 temp.append(nums[j])
        #                 temp.append(nums[k])
        #                 triplets.append(list(temp))

        # Remove dupticates.
        temp = []
        for triplet in triplets:
            if triplet not in temp:
                temp.append(triplet)

        triplets = temp

        return triplets
    


if __name__ == "__main__":
    solution = Solution()
    result = solution.threeSum([-1,0,1,2,-1,-4])
    print(result)
    result2 = solution.threeSum([0,1,1])
    print(result2)
    result3 = solution.threeSum([0,0,0])
    print(result3)
