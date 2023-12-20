class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            return digits[:-1]+[digits[-1]+1]
        digits=[0]+digits
        i=len(digits)-1
        while i>0 and digits[i]==9:
            digits[i]=0
            if digits[i-1]==8:
                digits[i-1]+=1
                break
            digits[i-1]+=(digits[i-1]!=9)
            i-=1 
        return digits[1:] if digits[0]==0 else digits