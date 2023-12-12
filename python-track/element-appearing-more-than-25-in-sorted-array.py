class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        return count.most_common(1)[0][0]
        