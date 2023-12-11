class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        t=len(nums)//3
        nums=sorted(list(set(nums)))
        return list(filter(lambda x: count[x]>t,nums))
        