class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        b=0
        f=0
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                f=i
                break
        for j in range(len(arr)-1,-1,-1):
            if arr[j]>=arr[j-1]:
                b=j
                break
        return b==f and b!=0 and f!=len(arr)-1 and len(arr)>2