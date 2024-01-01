class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr,i):
            j=0
            while j<i:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
                i-=1

        ans = []
        j=len(arr)-1

        while j>0:
            i= arr.index(j+1)
            if i!=j:
                flip(arr,i)
                ans.append(i+1)
                flip(arr,j)
                ans.append(j+1)
            j-=1
        return ans
        

        