class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        def backtrack(idx, subset):
            
            ans.add(tuple(subset[:]))
            
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return ans