class Solution:
    def splitString(self, s: str) -> bool:
        def check(start):
            if start == len(s):
                return len(splitted) > 1
            
            for i in range(start, len(s)):
                num = int(s[start : i + 1])
                if splitted and splitted[-1] != num + 1:
                    continue
                
                splitted.append(num)
                if check(i + 1):
                    return True
                
                splitted.pop()

            return False

        splitted = []
        return check(0)
