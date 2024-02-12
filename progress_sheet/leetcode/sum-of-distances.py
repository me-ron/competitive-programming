class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[0]*n
        hash={}
        for i in range(n):
            if nums[i] in hash:
                pre[i]=abs(i-hash[nums[i]][0])*hash[nums[i]][1] + pre[hash[nums[i]][0]]
                hash[nums[i]]=(i,hash[nums[i]][1]+1)
            else:
                hash[nums[i]]=(i,1)
        
        suf=[0]*n
        hash={}
        for i in range(n-1,-1,-1):
            if nums[i] in hash:
                suf[i]=abs(i-hash[nums[i]][0])*hash[nums[i]][1] + suf[hash[nums[i]][0]]
                hash[nums[i]]=(i,hash[nums[i]][1]+1)
            else:
                hash[nums[i]]=(i,1)
        print(pre,suf)
        return [pre[i]+suf[i] for i in range(n)]