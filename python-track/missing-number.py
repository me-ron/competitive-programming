class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=(len(nums)*(len(nums)+1))//2
        return x-sum(nums)
        