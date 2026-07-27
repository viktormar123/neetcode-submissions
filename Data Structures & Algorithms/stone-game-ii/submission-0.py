class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]
        
        suffix_sum = [0 for _ in range(n)]
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i] 

        for M in range(1, n):
            for j in range(1, 2*M+1):
                if j < n:
                    dp[n-j][M] = sum(piles[-j:])

        for i in reversed(range(n)):
            for M in range(1, n+1):
                # BASE CASE: If player can take all remaining piles, take them!
                if i + 2 * M >= n:
                    dp[i][M] = suffix_sum[i]
                else:
                    max_stones = 0
                    for X in range(1, 2*M+1):
                        value = suffix_sum[i] - dp[i+X][min(n, max(M,X))]
                        if value > max_stones:
                            max_stones = value

                    dp[i][M] = max_stones

        return dp[0][1]