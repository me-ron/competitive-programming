class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_string = s[:spaces[0]]
        for i in range (len(spaces)):
            if i<len(spaces)-1:
                new_string +=" " + s[spaces[i]:spaces[i+1]]
            else:
                new_string +=" " + s[spaces[i]:]
        return new_string
        