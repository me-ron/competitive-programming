class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq=1
        temp=1
        nums=list(set(nums))
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                temp+=1
            else:
                temp=1
            seq=max(temp,seq)
        return seq if nums else 0


        