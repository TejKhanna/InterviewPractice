'''

QUESTION:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPos = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroPos] = nums[zeroPos], nums[i]
                zeroPos += 1