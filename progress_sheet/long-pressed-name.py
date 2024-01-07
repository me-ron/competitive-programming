class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0      
        while i <= len(name) and j < len(typed):
            if i < len(name) and typed[j] == name[i]:
                i += 1
                j += 1
            elif typed[j] == name[i-1] and i != 0:
                j += 1
            else:
                return False
            
        return i == len(name) and j == len(typed)
        