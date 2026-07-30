class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(startTime)
        m = max(startTime)
        
        sorted_triplets = sorted(zip(startTime, endTime, profit))
        startTime, endTime, profit = map(list, zip(*sorted_triplets))

        dp = [0]*(n+1)

        # define dp[i] maximum profit when you can select jobs i to n-1
        # choice is select job i or not

        for i in range(n-1, -1, -1):
            # we can select job i and then find the next index j that is allowed: profit[i] + dp[j]
            # or we don't select job i: dp[i+1]
            
            j = i + 1
            while j < n and endTime[i] > startTime[j]:
                j+=1
            
            dp[i] = max(profit[i] + dp[j], dp[i+1])
            
        return dp[0]

