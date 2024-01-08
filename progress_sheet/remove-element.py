class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hold=0
        for seek in range(len(nums)):
            if nums[seek]!=val:
                nums[hold]=nums[seek]
                hold+=1
        return hold