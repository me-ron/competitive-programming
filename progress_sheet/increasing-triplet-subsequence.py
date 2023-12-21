class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1=float("inf")
        num2=float("inf")
        for i in range(len(nums)):
            if nums[i]>num2:
                return True
            if nums[i]>num1:
                num2=min(num2,nums[i])
            num1=min(num1,nums[i]) 
        return False

        