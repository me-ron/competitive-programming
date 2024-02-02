class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        x=len(set(nums))
        ans=0
        i=0
        window=defaultdict(int)
        for j in range(len(nums)):
            window[nums[j]]+=1
            
            while len(window)==x:
                window[nums[i]]-=1
                if window[nums[i]]==0:
                    window.pop(nums[i])
                i+=1
            ans+=i
        return ans
                
        