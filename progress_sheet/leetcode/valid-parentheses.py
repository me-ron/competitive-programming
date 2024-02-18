class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(","}":"{","]":"["}
        for i in s:
            if i not in match:
                stack.append(i)
            elif stack and stack[-1] == match[i]:
                stack.pop()
            else:
                return False
        return not stack
                    
                    
        