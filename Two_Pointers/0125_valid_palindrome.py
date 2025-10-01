"""
Problem: Valid Palindrome (LeetCode #125)
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isPalindrome(self, s: str) -> bool:
    #clean string (keep only alphanumeric, lowercase)
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    
    #check palindrome
    return cleaned == cleaned[::-1]