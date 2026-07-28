class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_products = [nums[0]]
        suffix_products = [nums[n-1]]

        for idx in range(1, n-1):
            prefix_products.append(nums[idx]*prefix_products[idx-1])
            suffix_products.append(nums[n-1-idx]*suffix_products[idx-1])

        output = [suffix_products[n-2]]
        for idx in range(0, n-2):
            output.append(prefix_products[idx]*suffix_products[n-3-idx]) 
        output.append(prefix_products[n-2])

        return output

