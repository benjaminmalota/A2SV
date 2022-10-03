class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0 
        r = 1
        profit = []
        
        while r < len(prices):
            if prices[l] < prices[r] or prices[l] == prices[r] :
                curr = prices[r] - prices[l]
                profit.append(curr)
                r+=1
            else:
                l += 1
        
        while profit:
            return max(profit)
        if profit == []:
            return 0

                
                
            