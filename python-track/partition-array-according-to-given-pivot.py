class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        def sorter(num):
            if num<pivot:
                return -1
            elif num==pivot:
                return 0
            else:
                return 1
        nums.sort(key= sorter)
        return nums
        