from typing import List


class Solution(object):
    def twoSum(self, nums: List, target: int) -> List:
        """Algorithm to find indexes of two numbers whose sum equals to the target number.
        Youtube explanation : https://www.youtube.com/watch?v=KLlXCFG5TnA

        Args:
            nums (List[int]): array containing numbers
            target (int): target number

        Returns:
            List: containing the indexes
        """

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
