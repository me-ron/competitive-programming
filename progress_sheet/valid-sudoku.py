class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        c=list(zip(*board))
        for i in range(n):
            s=set()
            for j in range(n):
                if board[i][j]!='.' and board[i][j] in s:
                    return False
                s.add(board[i][j])
        for i in range(n):
            s=set()
            for j in range(n):
                if c[i][j]!='.' and c[i][j] in s:
                    return False
                s.add(c[i][j])
        x=0
        while x<9:
            y=0
            while y<9:
                s=set()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[i][j]!='.' and board[i][j] in s:
                            return False
                        s.add(board[i][j])
                y+=3
            x+=3
        return True
        