"""
Problem: Product of Array Except Self (LeetCode #238)
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""


def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    output = [1]*n                 #initialise output array 

    #lets say nums = [1,2,3,4]

    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]          #output now = [1,1,2,6]

    # Explanation:
    # - "prefix" keeps track of the product of all elements BEFORE index i.
    # - At index i, we set output[i] = prefix.
    # - Then we update prefix by multiplying in nums[i].
    # - After this loop, output[i] contains the product of everything before i.
    
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]         

    # Explanation:
    # - "suffix" keeps track of the product of all elements AFTER index i.
    # - At index i, we multiply output[i] (which already has the prefix product)
    #   by suffix (the product of everything after i).
    # - Then we update suffix by multiplying in nums[i].
    # - After this loop, output[i] = prefix[i] * suffix[i], which is the full answer. 

    return output