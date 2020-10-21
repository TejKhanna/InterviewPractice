'''

QUESTION:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if len(numbers) == 0:
            return
        
        slow = 0
        fast = len(numbers) - 1
        
        while slow < fast:
            summation = numbers[slow] + numbers[fast]
            if summation == target:
                return [slow+1,fast+1]
            elif summation < target:
                slow += 1
            else:
                fast -= 1

