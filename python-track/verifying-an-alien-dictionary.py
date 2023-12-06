class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {char: i for i, char in enumerate(order)}
        def is_sorted(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    return order_index[word1[i]] < order_index[word2[i]]
            return len(word1) <= len(word2)

        for i in range(len(words)-1):
            if not is_sorted(words[i],words[i+1]):
                return False
        return True
    
        