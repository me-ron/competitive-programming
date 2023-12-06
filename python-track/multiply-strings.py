class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            num=num[::-1]
            ans=0
            for i in range(len(num)):
                char=(ord(num[i])-48)*10**i
                ans+=char
            return ans
        def revert(num):
            ans=""
            if num==0:
                ans="0"
            while num>0:
                remainder=num%10
                ans+=str(remainder)
                num=num//10
            return ans[::-1]

        num1=convert(num1)
        num2=convert(num2)
        return revert(num1*num2)
                
        