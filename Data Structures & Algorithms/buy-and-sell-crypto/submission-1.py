class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 2 pointers l < r
        l, r = 0, 1
        max_diff = 0
        n = len(prices)

        while r < n:
            profit = prices[r] - prices[l]
            max_diff = max(profit, max_diff)

            # Pointer updates
            if profit > 0:
                r+=1
            else: # price r is the newest lowest price for all next r values
                l = r
                r+=1

        return max_diff
            
