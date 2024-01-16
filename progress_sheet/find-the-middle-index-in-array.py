class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        run=0
        total=sum(nums)
        for i in range(len(nums)):
            if total-run-nums[i]==run:
                return i
            run+=nums[i]
        return -1