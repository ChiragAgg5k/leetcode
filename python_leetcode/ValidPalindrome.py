class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """Checks palindrome, ignores any character not alphanumeric
        Youtube explanation : https://www.youtube.com/watch?v=jJXJ16kPFWg&t=295s

        Args:
            s (str): String to be checked

        Returns:
            bool: True if valid palindrome, else False
        """

        newStr = ""

        for i in s:
            if i.isalnum():
                newStr += i.lower()

        return newStr == newStr[::-1]
