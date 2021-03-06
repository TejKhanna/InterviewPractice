'''

QUESTION:

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
                
        return i+1
            