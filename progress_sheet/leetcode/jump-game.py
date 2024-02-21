class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i <= reach:
                if i == len(nums) - 1:
                    return True
                reach = max(i + nums[i], reach)
        return False
        