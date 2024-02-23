class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue= deque()
        deck.sort()
        
        for i in range(len(deck)-1,-1,-1):
            if queue:
                x = queue.pop()
                queue.appendleft(x)
            queue.appendleft(deck[i])

        return queue