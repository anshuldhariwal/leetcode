class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        b = prices[0]

        for s in prices[1:]:
            if s > b:
                p = max(p, s - b)
            else:
                b = s

        return p

        
