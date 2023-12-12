class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        res = set(fronts).union(set(backs)) - set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])
        return min(res) if res else 0
            