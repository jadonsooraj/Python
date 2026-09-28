class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        if not intervals:
            return []
        intervals.sort(key = lambda x:x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if not (curr_start >= start and curr_start <= end):
                ans.append([start, end])
                start = curr_start
                end = curr_end
            else:
                end = max(curr_end,end)
        ans.append([start,end])
        
        return ans