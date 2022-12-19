class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """Checks if two strings are Anagrams.
        Two strings are considered Anagrams if they are made from the same no. of each letter
        Youtube explanation : https://www.youtube.com/watch?v=9UtInBqnCgA&t=640s

        Args:
            s (str): string 1
            t (str): string 2

        Returns:
            bool: True if Anagram, else False
        """

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
