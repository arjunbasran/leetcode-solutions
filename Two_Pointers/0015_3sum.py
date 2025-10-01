def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):                         #loops through array treating each number a, as the first element of a potential triplet
        if i > 0 and a == nums[i - 1]:                   #skips duplicates for the first element, e.g. if 2 consecutive numbers are the same we only want to use the first of the 2
            continue
        
        l, r = i + 1, len(nums) - 1                      #we set up 2 pointers that will search for the other 2 numbers
        while l < r:                                     #loop keeps going as long as the 2 pointers havent't crossed
            threeSum = a + nums[l] + nums[r]
            
            if threeSum > 0:                             #if sum is too big, we need a smaller value - move r to the left 
                r -= 1
            elif threeSum < 0:                           #if sum is too small, we need a bigger value - move l to the right
                l += 1
            else:
                res.append([a, nums[l], nums[r]])        #if sum is exactly 0 then we add triplet list to a list 
                l += 1                                   #we must force a change to prevent infinite loop and explore other potential triplets
                while nums[l] == nums[l - 1] and l < r:  #ensures that our change doesn't just lead to the same number and cause same effects as above - only breaks loop if nums[l] is diff
                    l += 1
                    
    return res