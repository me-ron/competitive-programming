class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, l, r):
            num = ""
            word = []
            open = 0
            while l < r :
                if s[l].isdigit():
                    num += s[l]
                elif s[l].isalpha():
                    word.append(s[l])
                else:
                    open += 1
                    x = l + 1
                    while l < r and open > 0:
                        l += 1
                        
                        if s[l] == "[":
                            open += 1
                        elif s[l] == "]":
                            open -= 1
                    num = int(num) if num else 1
                    word.append(num * decode(s, x , l))
                    num = ""

                l += 1
                
            num = int(num) if num else 1
            return ("".join(word)) * num

        return decode(s, 0, len(s))
        

        