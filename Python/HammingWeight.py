'''

QUESTION:
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)[2:]).count("1")