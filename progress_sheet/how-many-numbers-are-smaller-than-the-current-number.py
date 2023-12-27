class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[0]*101
        for i in nums:
            lst[i]+=1
        a=0
        b=0
        for i in range(101):
            a+=lst[i]
            lst[i]=b
            b=a

        for i in range(len(nums)):
            nums[i]=lst[nums[i]]
        return nums
        
        