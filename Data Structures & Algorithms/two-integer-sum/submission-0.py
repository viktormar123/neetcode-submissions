class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {} # maps complement of nums[idx] to idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in complements:
                return [complements[diff], idx]
            else:
                complements[num]=idx
        