class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}

        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        frequency_dict = dict(sorted(frequency_dict.items(), key=lambda x: -x[1]))
        output = []

        for idx, (num, frequency) in enumerate(frequency_dict.items()):
            if idx == k:
                break
            output.append(num)

        return output