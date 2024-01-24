class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pre=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
        for i in range(1,len(pre)):
            for j in range(1,len(pre[0])):
                pre[i][j] = matrix[i-1][j-1] + pre[i][j-1] 
        
        ans=0
        for j in range(1, len(pre[0])):
            for k in range(j, len(pre[0])):
                d = {0:1}
                sums = 0
                for i in range(1, len(pre)):
                    sums += pre[i][k] - pre[i][j-1]
                    ans += d.get(sums-target, 0)
                    d[sums] = d.get(sums, 0) + 1
        
        return ans


        return 0