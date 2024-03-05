class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i + 1 for i in range(9)]
        def help(idx):
            nonlocal n, k

            x = sum(comb)
            if x > n or len(comb) > k:
                return
            if x == n and len(comb) == k:
                ans.append(comb[:])
                return 
            
            for i in range(idx, len(nums)):
                if x + nums[i] > n:
                    return 
                
                comb.append(nums[i])
                help(i + 1)
                comb.pop()

        ans = []
        comb = []

        help(0)
        return ans 
        