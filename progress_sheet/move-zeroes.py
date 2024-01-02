class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        hold=0
        seek=0
        while seek<len(nums):
            if nums[seek]!=0:
                nums[hold],nums[seek]=nums[seek],nums[hold]
                hold+=1
            seek+=1
        return nums

    