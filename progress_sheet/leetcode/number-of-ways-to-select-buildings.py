class Solution:
    def numberOfWays(self, s: str) -> int:
        oz=zo=0
        zeros=ones=0
        ans=0
        for i in range(len(s)):
            if s[i]=="0":
                zeros+=1
                oz+=ones
                ans+=zo
            else:
                ones+=1
                zo+=zeros
                ans+=oz
        return ans

        

        