class Solution:
    def findMin(self, nums: List[int]) -> int:
        current_min = 1000
        

        first_value = nums[0]
        last_value = nums[-1]

        if last_value > first_value: # list is ordered already
            return nums[0]
        else: # binary search
            l = 0
            r = len(nums) - 1
        
            while l <= r:
                m = l + (r-l) // 2

                new_value = nums[m]

                if new_value < current_min:
                    current_min = new_value

                if new_value > last_value:
                    l = m + 1
                elif new_value < last_value:
                    r = m - 1
                else: # values are equal, ie m == len(nums) - 1
                    break

            return current_min
