class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        c = []
        if len(prices) == 1:
            return 0
        for i in range (len(prices)):
            for j in range (i):
                c.append(prices[i]-prices[j])
        if max(c) >= 0:
            return max(c)
        else:
            return 0 
        