class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # divide and conquer: List at index i, if L[i] 
        n = mountainArr.length()
        bottom = 0
        top = n - 1
        output = -1


        while bottom <= top:
            middle = (top + bottom) // 2
            value = mountainArr.get(middle)
            left_value = mountainArr.get(middle-1)                
            right_value = mountainArr.get(middle+1)

            if left_value < value and value > right_value:
                break_point = middle
                break
            elif left_value < value < right_value:
                bottom = middle + 1
            else:
                top = middle - 1
                
        # 2 binary searches, the first increasing list and the second decreasing list
        # Select the min idx 
        # increasing subset from 0 to break_point
        top = break_point
        bottom = 0
        increasing_idx = -1
        while bottom <= top:
            middle = (top + bottom) // 2
            value = mountainArr.get(middle)
            if value == target:
                increasing_idx = middle
                break
            elif value < target:
                bottom = middle + 1
            else:
                top = middle - 1

        bottom = break_point
        top = n - 1
        decreasing_idx = -1
        while bottom <= top:
            middle = (top + bottom) // 2
            value = mountainArr.get(middle)
            if value == target:
                decreasing_idx = middle
                break
            elif value < target:
                top = middle - 1
            else:
                bottom = middle + 1

        if min(increasing_idx, decreasing_idx) == -1:
            return max(increasing_idx, decreasing_idx)
        else:
            return min(increasing_idx, decreasing_idx)
