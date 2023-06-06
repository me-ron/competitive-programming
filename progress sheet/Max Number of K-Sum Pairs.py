from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic=Counter(nums)
        ans=0
        for i in dic:
            if i==k/2:
                ans+=floor(dic[i]/2)
            else:
                ans+=(min(dic[i],dic[k-i]))/2
        return int(ans)
