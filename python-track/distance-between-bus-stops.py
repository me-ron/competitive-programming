class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        small=min(start,destination)
        big=max(start,destination)
        dis=sum(distance[small:big])
        return min(dis,sum(distance)-dis)

        