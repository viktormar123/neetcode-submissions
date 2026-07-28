class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        for num in nums:
            product *= num
        
        output = []
        for idx, num in enumerate(nums): 
            if num != 0:
                output.append(int(product / num))
            if num == 0:
                value = 1
                for idx2, num2 in enumerate(nums):
                    if idx2 != idx:
                        value *= num2
                output.append(int(value))
        return output