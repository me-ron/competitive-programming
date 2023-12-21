class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=nums.count(1)
        before=0
        zeros=0
        dic={}
        big=0
        for i in range(len(nums)):
            dic[i]=zeros+(ones-before)
            big=max(big,dic[i])
            zeros+=(nums[i]==0)
            before+=(nums[i]==1)
        dic[len(nums)]=zeros+(ones-before)
        big=max(big,dic[len(nums)])
        return [i for i in dic if dic[i]==big]

        