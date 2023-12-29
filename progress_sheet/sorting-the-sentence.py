class Solution:
    def sortSentence(self, s: str) -> str:
        st=s.split()
        st.sort(key=lambda x: x[-1])
        st=[x[:-1] for x in st]
        return " ".join(st)