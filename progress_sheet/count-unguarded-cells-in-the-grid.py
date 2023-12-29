class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for i in range(m)]
         
        for i,j in walls:
            grid[i][j]=3
        for i,j in guards:
            grid[i][j]=2

        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        for x,y in guards:
            for h in dir:
                a, b=x+h[0],y+h[1]
                while 0<=a<m and 0<=b<n and grid[a][b] not in [2,3]:
                    grid[a][b]=1
                    a+=h[0]
                    b+=h[1]
                    
        ans=0
        for i in range(m):
            for j in range(n):
                ans+=(grid[i][j]==0)
        return ans
        