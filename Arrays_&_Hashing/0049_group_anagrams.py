"""
Problem: Group Anagrams (LeetCode #49)
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    seen = {}
    
    for i in strs:
        key = "".join(sorted(i))
        if key not in seen:
            seen[key] = [i]
        else:
            seen[key].append(i)
    
    
    return(list(seen.values()))