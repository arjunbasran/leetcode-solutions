"""
Problem: Two Sum II - Input Array Is Sorted (LeetCode #167)
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (index1, index2) as an integer array answer of size 2, where 1 <= index1 < index2 <= numbers.length.
"""


def twoSum(self, numbers: list[int], target: int) -> list[int]:
#hashmap method
    seen = {}
    for index, i in enumerate(numbers):
        diff = target - i
        if diff not in seen:
            seen[i] = index
        else:
            return [seen[diff] + 1 , index + 1] 


#better two pointers method that utilises the fact that the array is already sorted in ascending order
def twoSum(self, numbers: list[int], target: int) -> list[int]:     
    
    left, right = 0, len(numbers)-1      #tuple unpacking -> l = 0, r = len(numbers)-1
    
    while left < right:
        s = numbers[left] + numbers[right]

        if s == target:
            return [left + 1, right + 1]
        
        elif s > target:
            right -= 1
        
        else:
            left += 1