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