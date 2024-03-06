class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(i, j, num):
            return not(rows[i][num] or cols[j][num] or box[i//3][j//3][num])
        
        def place(i, j, num):
            board[i][j] = str(num + 1)
            rows[i][num] = cols[j][num] = box[i//3][j//3][num] = True
        
        def remove(i, j, num):
            board[i][j] = "."
            rows[i][num] = cols[j][num] = box[i//3][j//3][num] = False

        def backtrack():

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(9):
                            if is_valid(i, j, num):
                                place(i, j, num)
                                if backtrack():
                                    return True
                                remove(i, j, num)
                        return False
            
            return True
                   
            
        rows = [[False] * 9 for row in range(9)]
        cols = [[False] * 9 for col in range(9)]
        box = [[[False] * 9 for col in range(3)] for row in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    rows[i][num] = cols[j][num] = box[i//3][j//3][num] = True

        backtrack()


    