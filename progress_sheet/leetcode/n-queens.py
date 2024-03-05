class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(i, j):
            if j in attacked_cols or i - j in attacked_n_diagonal or i + j in attacked_m_diagonal:
                return False
            else:
                return True
        
        def place(i, j):
            comb[i][j] = "Q"
            attacked_cols.add(j)
            attacked_m_diagonal.add(i + j)
            attacked_n_diagonal.add(i - j)

        def remove(i, j):
            comb[i][j] = "."
            attacked_cols.remove(j)
            attacked_m_diagonal.remove(i + j)
            attacked_n_diagonal.remove(i - j)

        def backtrack(row):
            nonlocal n
            if row == n:
                x = ["".join(row_x) for row_x in comb]
                ans.append(x)
                return
                
            for col in range(n):
                if can_place(row, col):
                    place(row, col)
                    backtrack(row + 1)
                    remove(row, col)
            
        attacked_cols = set()
        attacked_m_diagonal = set()
        attacked_n_diagonal = set()

        ans = []
        comb = [["."] * n for i in range(n)]
        backtrack(0)

        return ans
        