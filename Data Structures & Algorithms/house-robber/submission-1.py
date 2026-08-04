class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            elif i == 0:
                return nums[i]
            elif i == 1:
                return max(nums[0], nums[1])
            else:
                value = max(nums[i] + dp(i-2), dp(i-1))
                memo[i] = value
                return value

        return dp(len(nums)-1)