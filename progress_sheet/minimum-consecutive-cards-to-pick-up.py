class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        i=0
        st={}
        ans=float('inf')
        for j in range(len(cards)):
            if cards[j] in st:
                ans=min(ans,j-st[cards[j]]+1) 
            st[cards[j]]=j
        return ans if ans!=float('inf') else -1
        