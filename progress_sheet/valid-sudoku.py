class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        ans=[]
        for i in range(n):
            for j in range(n):
                x=board[i][j]
                if x !='.':
                    ans+=[(i,x),(x,j),(i//3,j//3,x)]
        return len(ans)==len(set(ans))
        