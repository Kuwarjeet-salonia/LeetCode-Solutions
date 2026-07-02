class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = prices[0] 
        profit = 0 
        ans = 0 
        for i in range (len(prices)):
            if prices[i] < left:
                left = prices[i]
            if left < prices[i]:
                ans = (prices[i]-left)
            if ans > profit:
                profit = ans
        return profit