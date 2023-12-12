class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        num={n:idx for idx,n in enumerate(nums)}
        for i in range(len(nums)):
            p = target-nums[i]
            if p in num:
                a=num[p]
                if a==i:
                    continue
                break
        return i,a