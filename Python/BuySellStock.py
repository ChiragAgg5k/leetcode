from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        """Algorithm to find maximum profit on buying and selling stocks
         Youtube explaination : https://www.youtube.com/watch?v=1pkOgXD63yU&feature=emb_title

        Args:
            prices (List[int]): Array of prices, each index representing a day

        Returns:
            int: maximum possible profit that can be made
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
