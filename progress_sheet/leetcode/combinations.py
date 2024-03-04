class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def explore(num, combinations):
            nonlocal n

            if len(combinations) == k:
                ans.append(combinations[:])
                return
            
            if num > n:
                return 
            
            combinations.append(num)
            explore(num + 1, combinations)
            combinations.pop()

            explore(num + 1, combinations)

        ans = []
        explore(1, [])
        return ans
            
        