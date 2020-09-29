'''

QUESTION:
Given a 32-bit signed integer, reverse digits of an integer.

'''

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        num = abs(x)
        while num:
            num, digit = divmod(num, 10)
            result = result*10 + digit
        if result > 2**31-1:  
            return 0
        return result if x > 0 else -result