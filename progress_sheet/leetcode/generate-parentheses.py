class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open, close):
            if open == close == n:
                ans.append("".join(comb))

            if open < n:
                comb.append("(")
                backtrack(open + 1, close)
                comb.pop()

            if close < open:
                comb.append(")")
                backtrack(open, close + 1)
                comb.pop()
        
        ans = []
        comb = []
        backtrack(0, 0)

        return ans
