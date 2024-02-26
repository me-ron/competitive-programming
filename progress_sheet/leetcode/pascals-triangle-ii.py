class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex - 1)

        ans = [1]
        for i in range(1,len(prev)):
            ans.append(prev[i] + prev[i-1])
        ans.append(1)
        
        return ans