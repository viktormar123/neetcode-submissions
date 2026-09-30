class Solution:
    def rob(self, nums: List[int]) -> int:
        # It is a cycle, so it is symmetric no matter what starting point we choose
        # Can we pick a point that will always be picked? 
        # Probably not but if it is not picked, can we assume something else is picked?
        # I mean for a sequence A B C D E you should never skip a sequence of 3 digits like B C D
        # Therefore for any 3 adjacent houses you will always rob the middle one if the two others are not robbed
        # If the middle one is not robbed, then either B or D must be robbed.

        # So maximum over all houses 0, 1, 2, 3, ... n-1

        # We can also look at it this way when we have found a house that is not robbed, we can look at the rest of the sequence and treat it as a non cycle

        # So simply take max of dp when 0 is robbed and when it is not robbed?

        memo = dict()
        n = len(nums)

        def dp_with_0(i):
            if i in memo:
                return memo[i]
            elif i == 0:
                memo[i] = nums[0] + dp_with_0(2)
                return memo[i]
            elif i == 1:
                memo[i] = 0 + dp_with_0(2)
                return memo[i]
            elif i >= n:
                return 0
            elif i == n-1:
                return 0
            elif i == n-2:
                return nums[i]
            else:
                if n > i+1:
                    value = max(nums[i] + dp_with_0(i+2), nums[i+1] + dp_with_0(i+3))
                else:
                    value = nums[i] + dp_with_0(i+2)
                memo[i] = value
                return value

        memo_without_0 = dict()

        def dp_without_0(i):
            if i in memo_without_0:
                return memo_without_0[i]
            elif i == 0:
                memo_without_0[i] = dp_without_0(2)
                return memo_without_0[i]
            elif i == 1:
                memo_without_0[i] = nums[1] + dp_without_0(3)
                return memo_without_0[i]
            elif i >= n:
                return 0
            else:
                if n > i+1:
                    value = max(nums[i] + dp_without_0(i+2), nums[i+1] + dp_without_0(i+3))
                else:
                    value = nums[i] + dp_without_0(i+2)                
                memo_without_0[i] = value
                return value





        # Define function of i as the amount of money you can make using indexes i, ... n-1
        # f(0) is the output
        # f(i) = max(num[i] + f(i+2), num[i+1] + f(i+1))
        # initialize list all with 0
        # base values are f(n-1) = num[n-1] if num[0] is not allowed
        #                        = 

        dp_w_0 = [0]*(n+2)
        dp_wo_0 = [0]*(n+2)

        # When 0 is robbed, then it is dp of nums[2], ..., nums[n-2]
        # When 0 is not robbed, then it is dp of nums[1], ..., nums[n-1]

        dp_w_0[n-2] = nums[n-2]
        dp_wo_0[n-1] = nums[n-1]

        for j in range(n-3, 1, -1):                
            dp_w_0[j] = max(dp_w_0[j+2] + nums[j], dp_w_0[j+3] + nums[j+1])

        for j in range(n-2, 0, -1):
            dp_wo_0[j] = max(dp_wo_0[j+2] + nums[j], dp_wo_0[j+3] + nums[j+1])

        if n == 1:
            return nums[0]
        else:
            return max(nums[0] + dp_w_0[2], dp_wo_0[1])



        