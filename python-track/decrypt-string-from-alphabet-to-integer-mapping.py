class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        s=list(s)
        for i in s:
            if i=="#":
                ans[-2]+=ans[-1]
                ans.pop()
            else:
                ans.append(i)
        for i in range(len(ans)):
            ans[i]=chr(96+int(ans[i]))
        return "".join(ans)
        