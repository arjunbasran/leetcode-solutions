"""
Problem: Valid Anagrams (LeetCode #242)
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def isAnagram(s: str, t: str) -> bool:
    seen_s = {}
    seen_t = {}
    for i in s:
        if i in seen_s:
            seen_s[i] += 1
        else:
            seen_s[i] = 1
    
    for i in t:
        if i in seen_t:
            seen_t[i] += 1
        else:
            seen_t[i] = 1

    return seen_s == seen_t