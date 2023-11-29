class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])-1):
                if matrix[i-1][j]!=matrix[i][j+1]:
                    return False
        return True
        
        