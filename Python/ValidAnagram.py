'''

QUESTION:
Given two strings s and t , write a function to determine if t is an anagram of s.

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charList = []
        
        for a in s:
            charList.append(a)
        
        for i in t:
            # print(charList)
            if i in charList:
                charList.remove(i)
            else:
                return False
    
        # print(charList)
        if charList == []:
            return True