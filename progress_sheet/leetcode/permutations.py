class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                ans.append(perm[:])
                return
            if start > len(nums):
                return

            for i in range(len(nums)):
                if nums[i] in comb:
                    continue
                perm.append(nums[i])
                comb.add(nums[i])
                backtrack(start + 1)
                perm.pop()
                comb.remove(nums[i])

        perm = []
        comb = set()
        ans = []
        backtrack(0)
        return ans