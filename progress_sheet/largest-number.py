class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        nums.sort(key=lambda x: 10*x, reverse=True)
        return "".join(nums).lstrip("0") or "0"
        
        