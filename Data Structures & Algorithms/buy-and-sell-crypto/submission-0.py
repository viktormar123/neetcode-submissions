class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 2 pointers l < r
        l, r = 0, 1
        max_diff = 0
        n = len(prices)

        while l < n:
            if r >= n:
                if l < n-2:
                    l = l+1
                    r = l+1
                    continue
                else:
                    break
            if prices[l] > prices[l+1]:
                l+=1
                r+=1
                continue
            if r!= n-1 and prices[r] < prices[r+1]:
                r+=1
                continue

            current_diff = prices[r] - prices[l]
            if current_diff > max_diff:
                max_diff = current_diff
            
            if r == n-1:
                l+=1
                r = l + 1
            else:
                r+=1

        return max_diff
            
