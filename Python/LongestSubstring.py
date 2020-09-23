'''
QUESTION:
Given a string s, find the length of the longest substring without repeating characters.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        substring = ''
        longest_substring = ''
        
        
        for i in range(0,len(s)):
            if s[i] in substring:
                for j in range(0,len(substring)):
                    if s[i] == s[j]:
                        substring = substring[j+1:]+s[i]
                
            else:
                substring = substring + s[i]
            
            print("SS:" + substring)
            print("Longest:" + longest_substring)
        
            if len(substring) > len(longest_substring):
                longest_substring = substring
                
        return len(longest_substring)
