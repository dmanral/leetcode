"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Non decreasing order means duplicates are adjacent to each other and numbers are sorted in increasing order.
        # So essentially what we are doing is checking the 3rd number and if it is the same as the 1st number, we pop it out and check again until we have at most 2 duplicates.
        # Then we recurse until we have gone through the entire array and return the length of the array with at most 2 duplicates.
        for i in range(len(nums)):                      # Loops through the entire array.
            if i > 1 and nums[i] == nums[i - 2]:        # i > 1 skips the first 2 numbers since you need at least 2 elements before the current element to check for duplicates. If the current element is the same as the element 2 positions before it, then we have more than 2 duplicates.
                nums.pop(i)                             # Remove the current element since it is a duplicate and we want to keep at most 2 duplicates. We pop it out and check again until we have at most 2 duplicates.
                return self.removeDuplicates(nums)      # Recurse until we have gone through the entire array.
        return len(nums)                                # Return the length of the array with at most 2 duplicates.


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))