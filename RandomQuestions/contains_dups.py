def containsDuplicate(nums):
    numbSet = set(nums)
    if len(nums) != len(numbSet):
        return True
    else:
        return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([2,14,18,22,22]))