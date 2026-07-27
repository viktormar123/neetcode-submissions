class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_unique = set(nums)
        if len(nums_unique) != len(nums):
            return True
        else: return False