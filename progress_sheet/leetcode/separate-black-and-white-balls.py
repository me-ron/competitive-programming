class Solution:
    def minimumSteps(self, s: str) -> int:
        ans, ones = 0, 0
        for ball in s:
            if ball == "1":
                ones += 1
            else:
                ans += ones
        return ans
        