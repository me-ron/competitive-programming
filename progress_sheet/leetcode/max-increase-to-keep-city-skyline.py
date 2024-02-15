class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        n=len(grid)

        for i in range(n):
            for j in range(n):
                rows[i] = max(grid[i][j], rows[i])
                cols[i] = max(grid[j][i], cols[i])
        
        ans = 0
        for i in range(n):
            for j in range(n):
                diff = min(rows[i], cols[j])
                ans += diff - grid[i][j]

        return ans

        