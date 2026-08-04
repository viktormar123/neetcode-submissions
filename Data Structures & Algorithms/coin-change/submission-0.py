class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0] + [float("inf")]*amount
        
        for i in range(1, amount+1):
            min_num = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    current_num = dp[i-coin] + 1
                    if current_num < min_num:
                        min_num = current_num

            dp[i] =  min_num

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]

