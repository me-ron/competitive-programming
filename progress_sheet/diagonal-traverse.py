class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        ans=[]
        for i in dic:
            ans+=(dic[i] if i%2 else dic[i][::-1])
        return ans
        


        