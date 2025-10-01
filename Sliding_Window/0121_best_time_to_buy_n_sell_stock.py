"""
Problem: Best Time to Buy and Sell Stock (LeetCode #121)
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
"""

def maxProfit(self, prices: list[int]) -> int:
        
    max_profit = 0
    l, r = 0, 1                                     # l = buy price, r = sell price 

    while r < len(prices):
        
        if prices[r] < prices[l]:
            l = r                                   # if sell price < buy price, we have found a cheaper buying price so start from there
        
        else:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)    # max_profit keeps track of best profit so far
            r += 1
    
    return max_profit