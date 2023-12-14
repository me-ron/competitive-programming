class OrderedStream:

    def __init__(self, n: int):
        self.n = n 
        self.ans = [""] * self.n
        self.p = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ans[idKey - 1] = value
        while self.p < self.n and self.ans[self.p] != "":
            self.p += 1
        return self.ans[idKey - 1 : self.p]       


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)