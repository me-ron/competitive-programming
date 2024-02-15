class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        cols = len(matrix[0])+1
        rows = len(matrix)+1
        pre = [[0]*cols for i in range(rows)]

        for i in range(1,rows):
            for j in range(1,cols):
                pre[i][j] = pre[i][j-1] + matrix[i-1][j-1] + pre[i-1][j] -pre[i-1][j-1]
 
        ans=0
        for r1 in range(1,rows):
            for r2 in range(r1,rows):
                sums = defaultdict(int)
                sums[0] = 1
                for c in range(1,cols):
                    curr = pre[r2][c]-pre[r1-1][c]
                    diff = curr - target
                    ans += sums[diff]
                    sums[curr] += 1
                    
        return ans
        
        
