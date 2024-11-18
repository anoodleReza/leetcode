class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        comb = []
        print(intervals)

        for interval in intervals:
            # interval starts after previous
            if not comb or comb[-1][1] < interval[0]:
                comb.append(interval)
            else:
                comb[-1][1] = max(comb[-1][1], interval[1])
        return comb