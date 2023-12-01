class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        st=set()
        while n>0:
            x=(math.log10(n)/math.log10(3))
            x=int(x)
            if x in st:
                return False 
            st.add(x)
            n-=(3**x)
        return True

        