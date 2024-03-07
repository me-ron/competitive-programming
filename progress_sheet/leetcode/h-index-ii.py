class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = -1
        j = n

        while i + 1 < j:
            mid = (i + j) // 2

            if citations[mid] > n - mid:
                j = mid

            else:
                i = mid

        return max(citations[i], n - i - 1) if i > -1 else n


        