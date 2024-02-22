class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = Counter(s)
        stack = []
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and stack[-1] > s[i] and dic[stack[-1]] > 0:
                    seen.remove(stack.pop())
                stack.append(s[i])
            seen.add(s[i])
            dic[s[i]] -= 1
        return "".join(stack)