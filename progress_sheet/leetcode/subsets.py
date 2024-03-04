class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(idx, subset):
            
            ans.add(tuple(subset[:]))
            
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return ans