class Solution(object):
    def maxProfit(self, prices):
        """
        In this solution,
        we are implying a two pointer solution.
        Basically left pointer stays at LOWEST value 
        while right pointer traverses after that left pointer checking the profit gap.
        """

        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return maxProfit
