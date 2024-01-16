class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s=list(s)
        pre=[0]*len(s)
        for x,y,z in shifts:
            if z:
                pre[x]+=1
                if y+1<len(s):
                    pre[y+1]-=1

            else:
                pre[x]-=1
                if y+1<len(s):
                    pre[y+1]+=1

        run=0
        for i in range(len(s)):
            run+=pre[i]
            pre[i]=run
            s[i]=ord(s[i])+pre[i]
            y=(s[i]-96)%26 or 26
            s[i]=chr(y+96)
        return "".join(s)
