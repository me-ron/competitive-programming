class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(i, j):
            if j in attacked_cols or i - j in attacked_n_diagonal or i + j in attacked_m_diagonal:
                return False
            else:
                return True
        
        def place(i, j):
            attacked_cols.add(j)
            attacked_m_diagonal.add(i + j)
            attacked_n_diagonal.add(i - j)

        def remove(i, j):
            attacked_cols.remove(j)
            attacked_m_diagonal.remove(i + j)
            attacked_n_diagonal.remove(i - j)

        def backtrack(row, count):
            nonlocal n

            for col in range(n):

                if can_place(row, col):

                    place(row, col)
                    if row == n - 1:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove(row, col)
                
            return count

        attacked_cols = set()
        attacked_m_diagonal = set()
        attacked_n_diagonal = set()
        ans = backtrack(0, 0)
        return ans
        