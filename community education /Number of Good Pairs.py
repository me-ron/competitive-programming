class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        g_pairs=0
        for i in range(len(nums)):
            for j in range (len(nums)):
                if nums[i]==nums[j] and i<j:
                    g_pairs+=1
        return g_pairs
