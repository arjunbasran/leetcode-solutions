"""
Problem: Contains Duplicate (LeetCode #217)
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

# Uses a set to keep track of numbers we've already seen.
# If we encounter a number that's already in the set, return True.
# Otherwise, add the number to the set and keep going.
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Shorter version using set properties:
# If the list has duplicates, converting it to a set will remove them.
# So if lengths differ, that means duplicates existed.
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
