class Solution(object):
    def isValid(self, s: str) -> bool:

        """Checks if given set of parentheses are valid or not.
        Youtube explanation : https://www.youtube.com/watch?v=WTzjTskDFMg

        Returns:
            bool: True if valid, else False
        """

        match = {")": "(", "}": "{", "]": "["}
        l = []

        for i in s:
            if i not in match:
                l.append(i)
                continue

            if not l or l[-1] != match[i]:
                return False
            l.pop()

        # returns true if l is empty
        return not l
