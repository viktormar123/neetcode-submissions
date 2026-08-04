import sys
sys.setrecursionlimit(10000)

class Solution:
    def climbStairs(self, n: int) -> int:


        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            elif i == 1 or i == 0:
                return 1
            else:
                memo[i] = dp(i-1) + dp(i-2)
                return memo[i]
        
        return dp(n)