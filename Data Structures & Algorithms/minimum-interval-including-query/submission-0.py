class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #intervals = sorted(intervals, key lambda x: x[0])
        output = [0]*len(queries)
        for i, q in enumerate(queries):
            minimum = -1
            for inter in intervals:
                left_i = inter[0]
                right_i = inter[1]
                if left_i <= q <= right_i:
                    new_len = right_i - left_i + 1
                    if minimum == -1:
                        minimum = new_len
                    elif minimum > new_len:
                        minimum = new_len
            output[i]=minimum
        return output

