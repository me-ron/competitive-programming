class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def explore(pos, path):
            nonlocal n, k
            if len(path) == k:
                ans.append(path[:])
                return
            
            for num in range(pos, n + 1):
                path.append(num)
                explore(num + 1, path)
                path.pop()
        
        explore(1, [])
        return ans
            
        