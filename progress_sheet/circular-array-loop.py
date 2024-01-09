class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        nxt= lambda x : (x+nums[x])%len(nums)
        for i in range(len(nums)):
            j=i
            visited=set()
            while j not in visited and nums[nxt(j)]*nums[j]>0:
                visited.add(j)
                j=nxt(j)
            if j==i and len(visited)>1:
                return True
        return False
            
        
        