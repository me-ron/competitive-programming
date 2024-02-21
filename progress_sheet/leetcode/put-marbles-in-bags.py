class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ans = sorted([weights[i] + weights[i+1] for i in range(len(weights)-1)])
        print(ans)
        return sum(ans[-k+1 or len(ans):]) - sum(ans[:k-1]) 