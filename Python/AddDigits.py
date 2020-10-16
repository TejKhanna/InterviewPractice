'''

QUESTION:
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

'''

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0