class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        e_sum=sum([i for i in nums if i%2==0])
        ans=[]
        for i in (queries):
            if nums[i[1]]%2==0:
                e_sum-=nums[i[1]]
            nums[i[1]]+=i[0]
            if nums[i[1]]%2==0:
                e_sum+=nums[i[1]]
            ans.append(e_sum)   
        return ans
            
        