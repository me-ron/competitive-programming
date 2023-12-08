class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={indices[i]:s[i] for i in range (len(s))}
        dic={key: val for key, val in sorted(dic.items(), key = lambda x: x[0])}
        return "".join(dic.values())