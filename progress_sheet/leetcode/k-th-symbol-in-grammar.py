class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def reversed(n, k, ans):
            if n == 1:
                return ans
            half = (2**(n - 1))//2
            if k > half:
                ans += 1
                k -= half
            return reversed(n - 1, k, ans)
        
        return reversed(n, k, 0) % 2
    