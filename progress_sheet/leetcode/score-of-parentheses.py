class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                score = 0
                while stack and stack[-1] != "(":
                    score += stack[-1] 
                    stack.pop()
                score = 2*score if score else 1
                stack.pop()
                stack.append(score)

        return sum(stack)
        