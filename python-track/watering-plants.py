class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        hold=capacity
        for i in range(len(plants)):
            ans+=1
            if capacity<plants[i]:
                ans+=i*2
                capacity=hold
            capacity-=plants[i]
        return ans

        