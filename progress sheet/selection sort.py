class Solution: 
    def select(self, arr, i):
        starting_index=i
        for index in range(i,len(arr)):
            if arr[index] <= arr[starting_index]:
                   starting_index = index
        return starting_index
    
    def selectionSort(self, arr,n):
         for i in range(len(arr)):
            starting_index = self.select(arr,i)
            arr[starting_index],arr[i]=arr[i],arr[starting_index]
         return arr
