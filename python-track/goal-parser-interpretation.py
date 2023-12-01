class Solution:
    def interpret(self, command: str) -> str:
        st=""
        temp=""
        for i in range(len(command)):
            temp+=command[i]
            if temp=="G":
                st+="G"
                temp=""
            elif temp=="()":
                st+="o"
                temp=""
            elif temp=="(al)":
                st+="al"
                temp=""
        return st
        