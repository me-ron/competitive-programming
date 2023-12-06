class Solution:
    def totalMoney(self, n: int) -> int:
        q=n//7
        r=n%7
        w_sum=q*(56+(q-1)*7)//2
        d_sum=r*(2*(q+1)+r-1)//2
        return w_sum+d_sum if r else w_sum
        