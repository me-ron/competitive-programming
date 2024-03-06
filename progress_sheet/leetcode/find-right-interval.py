class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        search = sorted([(intervals[i][0], i)for i in range(n)])
        index = [search[i][1] for i in range(n)]
        search = [search[i][0] for i in range(n)]

        ans = [-1] * n
        for i in range(n):
            start, end = intervals[i]
            idx = bisect_left(search, end)
            if idx < len(intervals):
                ans[i] = index[idx]
        
        return ans
        