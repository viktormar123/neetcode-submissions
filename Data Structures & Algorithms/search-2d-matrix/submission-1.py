class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        row_m = matrix[m]
        l, r = 0, len(row_m) - 1

        while l <= r:
            m = l + (r - l) // 2

            value = row_m[m]

            if value == target:
                return True
            elif value < target:
                l = m + 1
            else: 
                r = m - 1
        
        return False