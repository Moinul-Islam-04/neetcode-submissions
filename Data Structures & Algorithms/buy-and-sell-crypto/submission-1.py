class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        B, S = 0, 1
        maxP = 0

        while S < len(prices):
            if prices[B] < prices[S]:
                profit = prices[S] - prices[B]
                maxP = max(maxP, profit)
            else:
                B = S
        
            S += 1

        return maxP

            