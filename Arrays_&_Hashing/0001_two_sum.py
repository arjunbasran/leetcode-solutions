"""
Problem: Two Sum (LeetCode #1)
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
"""

# Brute force O(n^2)
def twoSum_Bruteforce(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimised O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
