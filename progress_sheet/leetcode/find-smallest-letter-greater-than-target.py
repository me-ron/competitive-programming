class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters) - 1
        while i <= j:
            mid = (i + j) // 2
            if letters[mid] > target:
                j = mid - 1

            else:
                i = mid + 1

        if i < len(letters):
            return letters[i]
        return letters[0]