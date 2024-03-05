class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def back(i, j, idx, visited):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False

            if board[i][j] != word[idx] or (i, j) in visited:
                return False

            visited.add((i, j))
            
            top = back(i - 1, j, idx + 1, visited)
            left = back(i, j - 1, idx + 1, visited)
            bottom = back(i + 1, j, idx + 1, visited)
            right = back(i, j + 1, idx + 1, visited)

            visited.remove((i, j))
            
            return top or left or bottom or right
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if back(i, j, 0, set()):
                        return True
        
        return False

        