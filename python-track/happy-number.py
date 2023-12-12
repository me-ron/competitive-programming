class Solution:
    def isHappy(self, n: int) -> bool:
        def process(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n = n // 10
            return s
        st=set()
        while n not in st:
            st.add(n)
            n=process(n)
            if n==1:
                return True
        return False

        