class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=list(set(nums1).intersection(set(nums2)))
        c1=Counter(nums1)
        c2=Counter(nums2)
        ans=[]
        for i in s:
            ans+=[i]*min(c1[i],c2[i])
        return ans

        