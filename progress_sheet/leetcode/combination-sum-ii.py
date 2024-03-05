class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def help(idx, end):
            nonlocal target
            x = sum(comb)
            if x == target:
                ans.add(tuple(comb[:]))
                return 
            if idx >= len(candidates) or end == candidates[idx]:
                return 
            
            for i in range(idx, len(candidates)):
                if x + candidates[i] > target:
                    return 
                comb.append(candidates[i])
                help(i + 1, end)
                end = comb.pop()

        ans = set()
        comb = []
        candidates.sort()

        help(0, 0)
        return ans
        