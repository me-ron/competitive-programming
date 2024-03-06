class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can(capacity, days):
            day = 1
            weight = weights[0]
            for j in range(1, len(weights)):
                if day > days or weight > capacity:
                    return False
                weight += weights[j]

                if weight > capacity:
                    weight = weights[j]
                    day += 1
            if day > days or weight > capacity:
                return False  

            return True
        
        left = 1
        right = sum(weights)

        while left + 1 < right:

            mid = (left + right) // 2

            if can(mid, days):
                right = mid 
            else:
                left = mid

        return right
                
        