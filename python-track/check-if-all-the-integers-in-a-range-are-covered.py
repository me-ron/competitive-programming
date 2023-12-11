class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ran={i for a,b in ranges for i in range(a,b+1)}
        return set(range(left,right+1))<=ran


        