class Solution:
    def smallestNumber(self, num: int) -> int:
        s=-1 if num<0 else 1
        if num>=0:
            num=list(str(num))
            num.sort()
            i=0
            while i<len(num):
                if num[i]!='0':
                    break
                i+=1
            if len(num)>1 and num[0]=='0':
                num[0],num[i]=num[i],num[0]
        else:
            num=list(str(num))[1:]
            num.sort(reverse=True)
        return int("".join(num))*s