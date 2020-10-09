'''

QUESTION:
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        numStr = ''
        sign = ''
        numRead = False
        
        #use int(str)
        
        s = s.strip()
        
        digits = '1234567890'
        
        for i in s:
            
            print(numStr)
            
            if i in '+-' and numRead == False: #asssign sign and start reading number
                sign = i
                numRead = True
                
            elif i in digits and numRead == False: 
                numStr += i
                numRead = True
                
            elif i not in '+-' and i not in digits and numRead == False:
                return 0
                  
            elif i in digits and numRead == True:
                numStr += i
                
            elif i not in digits and numRead == True:
                break
                
        if numStr != '':
            num = int(numStr)
            
        else:
            return 0
            
        if sign == '-':
            num = num * -1
            
        if num < -2**31:
            num = -2**31

        if num >= 2**31:
            num = 2**31 - 1
            
        return num