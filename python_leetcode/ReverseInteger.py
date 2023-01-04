class Solution:
    def reverse(self, x: int) -> int:
        """Leetcode 7. Reverse Integer
        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            x (int): Integer to be reversed

        Returns:
            int: Reversed integer
        """
        
        isNegative = x<0
        x = -x if isNegative else x

        rev_string = str(x)[::-1]
        rev_int = -int(rev_string) if isNegative else int(rev_string)
        
        if rev_int < -2**31 or rev_int > 2**31 - 1:
            return 0
        return rev_int
        
if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))