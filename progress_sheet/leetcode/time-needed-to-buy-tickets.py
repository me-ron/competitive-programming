class Solution:
    def timeRequiredToBuy(self, ticket: List[int], k: int) -> int:
        i = 0
        ans = 0
        n = len(ticket)
        while ticket[k] > 0:
            ans += ticket[i%n] > 0
            ticket[i%n] -= 1 if ticket[i%n] else 0
            i += 1
        return ans 
        