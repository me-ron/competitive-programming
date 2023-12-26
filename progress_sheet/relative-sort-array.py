class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={n:i for i,n in enumerate(arr2)}
        def sorter(n):
            if n in dic:
                return dic[n]
            else:
                return n+len(arr2)
        arr1.sort(key=sorter)
        return arr1