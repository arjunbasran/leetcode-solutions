"""
Problem: Container With Most Water (LeetCode #11)
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
"""

def maxArea(self, height: list[int]) -> int:
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:                                              #two pointers approach
        area = (right - left)*min(height[left], height[right])       #calculate area between the 2 pointers
        max_area = max(max_area, area)                               #update max_area if the current area is larger than the previous max_area

        if height[left] < height[right]:                             #move pointer left/right depending on which line is shorter
            left += 1
        else:
            right -= 1
        
    return max_area

#KEY LOGIC:
# The area is limited by the shorter line and the width between the lines.
# By moving the pointer of the shorter line inward, we have a chance to find a taller line.
# Area increases so long that the height of the shorter line increases enough to offset the decrease in width (>1).