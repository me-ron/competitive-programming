class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x + 1

        while i + 1 < j:
            mid = (i + j) // 2
            sqr = mid * mid
            if sqr <= x:
                i = mid
            else:
                j = mid
        
        return i
                