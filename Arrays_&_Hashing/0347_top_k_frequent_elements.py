"""
Problem: Top K Frequent Elements (LeetCode #347)
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
def topKFrequent(nums: list[int], k: int) -> list[int]:
    seen = {}
    for i in nums:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    pairs = list(seen.items())                                              #turns dict into list of key-value pairs
    sorted_pairs = sorted(pairs, key = lambda p: p[1], reverse = True)      #sorts list of pairs by value in descending order
    top = sorted_pairs[:k]                                                  #gets first k elements of sorted list
    return [num for num, _ in top]                                          #returns list of only the keys from the top k pairs

    #key things to note:
    #    lambda function does not need a return statement