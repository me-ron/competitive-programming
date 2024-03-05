class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def help(idx):

            if idx > len(digits):
                return 
            
            if len(comb) == len(digits):
                if comb:
                    ans.append("".join(comb))
                return

            for i in range(len(map[digits[idx]])):
                comb.append(map[digits[idx]][i])
                help(idx + 1)
                comb.pop()
        
        ans = []
        comb = []
        help(0)
        return ans
        