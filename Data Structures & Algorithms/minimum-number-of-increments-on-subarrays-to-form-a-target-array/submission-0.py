class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        num = target[0]
        n = len(target)
        for i in range(1, n):
            if target[i-1] < target[i]:
                num += target[i] - target[i-1]
        return num