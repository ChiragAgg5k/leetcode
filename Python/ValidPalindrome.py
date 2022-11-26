class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """Checks palindrome, ignores any character not alphanumeric

        Palindrome: Strings which remain the same on reversing the order. Eg. "taco cat".
        (we ignored the whitespace)

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
