class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # This is dp

        memo = {}
        n = len(cost)
        def dp(i):
            if i in memo:
                return memo[i]
            elif i == n-1:
                memo[i] = cost[n-1]
                return cost[n-1]
            elif i == n-2:
                memo[i] = cost[n-2]
                return cost[n-2]
            elif i >= n:
                return 0
            else:
                value = cost[i] + min(dp(i+1), dp(i+2))
                memo[i] = value 
                return value

        return min(dp(0), dp(1))