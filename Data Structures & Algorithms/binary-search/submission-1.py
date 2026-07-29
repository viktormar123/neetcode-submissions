class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = l + ((r - l) // 2)
            value = nums[m]

            if value == target:
                return m

            elif value < target:
                l = m+1
            else:
                r = m-1
        
        return - 1