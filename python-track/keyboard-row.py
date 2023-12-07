class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard=["qwertyuiop","asdfghjkl","zxcvbnm"]
        keyboard=list(map(list,keyboard))
        keyboard=list(map(set,keyboard))
        ans=[]
        for word in words:
            lower_word=word.lower()
            for row in keyboard:
                if set(lower_word).issubset(row):
                    ans.append(word)
                    break
        return ans

        