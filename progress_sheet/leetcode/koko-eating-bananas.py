class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(k, h):
            hour = 0
            for i in range(len(piles)):
                hour += ceil(piles[i] / k)

            return hour <= h
                
        
        left = 0
        right = max(piles)

        while left + 1 < right:

            mid = (left + right) // 2

            if can(mid, h):
                right = mid 
            else:
                left = mid

        return right
        