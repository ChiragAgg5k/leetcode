class Solution(object):

    def isAnagram(self, s, t):

        """
        In this solution we will first check if lengths of both the string are same
        Then we will create two hashmaps and store count of each letter in the string
        if hashmaps of both the strings are same , the strings are anagram.
        """
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT