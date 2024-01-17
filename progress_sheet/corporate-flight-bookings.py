class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*n
        for a,b,k in bookings:
            ans[a-1]+=k
            if b<n:
                ans[b]-=k
        for i in range(1,n):
            ans[i]+=ans[i-1]
        return ans
        