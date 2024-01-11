class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tf={"T":0,"F":0}
        ans=i=0
        for j in range(len(answerKey)):
            tf[answerKey[j]]+=1
            while tf["T"]>k and tf["F"]>k:
                tf[answerKey[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans

        