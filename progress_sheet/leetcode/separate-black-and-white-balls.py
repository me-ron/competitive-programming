class Solution:
    def minimumSteps(self, s: str) -> int:
        ans,ones=0,0
        for i in s:
            if i=="1":
                ones+=1
            else:
                ans+=ones
        return ans
        