class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        c = Counter(senate)
        queue = deque(senate)

        red, die = 0, 0
        while c["R"] and c["D"]:
            vote = queue.popleft()
            if vote == 'R':
                if red == 0:
                    die -= 1
                    c['D'] -= c['D'] > 0
                    queue.append(vote)
                else:
                    red += 1

            else:
                if die == 0:
                    red -= 1
                    c['R'] -= c['R'] > 0
                    queue.append(vote)
                else:
                    die += 1
            
        if not c['R']:
            return 'Dire'
        return 'Radiant'