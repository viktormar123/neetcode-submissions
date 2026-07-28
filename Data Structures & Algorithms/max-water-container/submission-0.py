class Solution:
    def maxArea(self, heights: List[int]) -> int:
                # the base will decrease
        # So to find a larger value of area later, we can't shift the index of the higher height
        # Let's call max the higher index and min the lower index
        # area is then (r - l) * min
        # shifting the max index will result in a new area with a smaller base and the height can also only get smaller
        # so not even worth iterating over those values,
        # Shifting the min index, will result in smaller base but the height can also increase 
        # if the newer height of the min index is higher than the previous height
        
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            h_l = heights[l]
            h_r = heights[r]

            current_area = (r-l) * min(h_l, h_r)
            if max_area < current_area:
                max_area = current_area
            
            if h_l <= h_r:
                new_l = l + 1
                while heights[new_l] < h_l and new_l < r:
                    new_l += 1
                l = new_l

            elif h_r < h_l:
                new_r = r - 1
                while heights[new_r] < h_r and new_r > l:
                    new_r -= 1
                r = new_r
        return max_area
