class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def help(idx):
            nonlocal target

            x = sum(comb)
            if x == target:
                ans.append(comb[:])
                return 
            
            for i in range(idx, len(candidates)):
                if x + candidates[i] > target:
                    return 
                
                comb.append(candidates[i])
                help(i)
                comb.pop()

        ans = []
        comb = []
        candidates.sort()

        help(0)
        return ans
        