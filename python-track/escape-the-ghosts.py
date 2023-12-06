class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        diff=abs(target[1])+abs(target[0])
        ghosts.sort(key= lambda x: abs(x[1]-target[1])+abs(x[0]-target[0]))
        g_diff=abs(ghosts[0][1]-target[1])+abs(ghosts[0][0]-target[0])
        return diff<g_diff