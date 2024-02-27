class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reversed(n, k, reverse):
            if n == 1:
                return reverse

            half = ((2**n) - 1) // 2
            if k == half + 1:
                return reverse + 1
            elif k > half + 1:
                reverse += 1
                k -= (half + 1)
                k = half - k + 1
            
            return reversed(n - 1, k, reverse)
        
        return str(reversed(n, k, 0) % 2)
        