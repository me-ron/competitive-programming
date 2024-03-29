class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pre=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
        for i in range(1,len(pre)):
            for j in range(1,len(pre[0])):
                pre[i][j] = matrix[i-1][j-1] + pre[i][j-1] 
        
        ans=0
        for j in range(1, len(pre[0])):
            for k in range(j, len(pre[0])):
                run = {0:1}
                sums = 0
                for i in range(1, len(pre)):
                    sums += pre[i][k] - pre[i][j-1]
                    if sums-target in run:
                        ans+=run[sums-target]
                    run[sums] = run.get(sums, 0)
                    run[sums]+=1
        
        return ans