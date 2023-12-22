class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ref=list(zip(*matrix))
        m=len(matrix)-1
        for i in range(len(matrix)):
            for j in range (len(matrix)):
                matrix[i][j]=ref[i][m-j]
                
        