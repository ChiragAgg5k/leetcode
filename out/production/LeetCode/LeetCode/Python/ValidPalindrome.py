class Solution(object):
    def isPalindrome(self, s):
        """
        In this solution, 
        we will just create a string only containing alphanumeric chars and lowercase them
        then check palindrome using [::-1] (yay python)
        """
        
        newstr = ""
        
        for i in s:
            if i.isalnum():
                newstr += i.lower()
        
        return newstr == newstr[::-1]