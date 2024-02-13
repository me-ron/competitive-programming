class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        x, y, di = 0, 0, 0  
        for _ in range(m * n):
            if head is None:
                break
            mat[x][y] = head.val
            head = head.next
            dx, dy = directions[di]
            if 0 <= x+dx < m and 0 <= y+dy < n and mat[x+dx][y+dy] == -1:
                x += dx
                y += dy
            else:  
                di = (di + 1) % 4
                dx, dy = directions[di]
                x += dx
                y += dy
        return mat
