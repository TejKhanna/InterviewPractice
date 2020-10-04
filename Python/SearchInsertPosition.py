'''

QUESTION:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    return i
                
        else:
            
            for i in range (0, (len(nums)-1)):
                if i == len(nums):
                    return i+1
                if (nums[i] < target) & (nums[i+1] > target):
                    return i+1