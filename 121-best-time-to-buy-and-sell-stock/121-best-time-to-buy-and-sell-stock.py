class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        else:
            maximum = 0
            minimum = prices[0]
            for i in range(len(prices)):
                profit = prices[i] - minimum
                maximum = max(profit, maximum)
                minimum = min(minimum, prices[i])

            return maximum