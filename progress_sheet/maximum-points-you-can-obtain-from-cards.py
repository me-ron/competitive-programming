class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        temp=sum(cardPoints[:k])
        ans=temp
        i,j=k-1,len(cardPoints)-1
        while i>=0:
            temp-=cardPoints[i]
            temp+=cardPoints[j]
            i-=1
            j-=1
            ans=max(ans,temp)
        return ans
            

        