class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if not n or n%3 != 0:
            return False
        else:
            return self.isPowerOfThree(n // 3)
        