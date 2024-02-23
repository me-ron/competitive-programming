class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = float("-inf")

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i] > stack[-1]:
                second = stack.pop()
            
            if nums[i] < second:
                return True

            stack.append(nums[i])
        return False
        