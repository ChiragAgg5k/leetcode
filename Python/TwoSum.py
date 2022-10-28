class Solution(object):
    def twoSum(self,nums, target):
        
        """
        In this solution,
        we will just save the index and value of each element as a "value:index" pair.
        at the same time we will look for the integer which on addition makes our target int
        """

        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i