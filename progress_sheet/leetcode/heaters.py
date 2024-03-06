class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0

        for house in houses:
            idx = bisect_left(heaters, house)
            if 0 < idx < len(heaters):
                ans = max(ans, min(heaters[idx] - house, house - heaters[idx - 1]))
            elif idx == 0:
                ans = max(ans, heaters[idx] - house)
            else:
                ans = max(ans, house - heaters[idx - 1])
        
        return ans
