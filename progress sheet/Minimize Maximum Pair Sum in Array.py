class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        nums.sort()
        lst=[]
        while i<j:
            lst.append(nums[i]+nums[j])
            i+=1
            j-=1
        lst.sort()
        return lst[-1]
