class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        l=sorted(nums)
        dic={}
        for i in range (len(l)):
            if l[i] not in dic:
                dic[l[i]]=i
        for i in nums:
            lst.append(dic[i])
        return lst
        
        