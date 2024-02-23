class MinStack:

    def __init__(self):
        self.mainStack=[]
        self.minStack=[]    

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if self.minStack:
            if self.minStack[-1]>=val:
                self.minStack.append(val)
        else:
            self.minStack.append(val)
            
    def pop(self) -> None:
        m=self.mainStack.pop()
        if self.minStack[-1]==m:
            self.minStack.pop()
        
    def top(self) -> int:
        return self.mainStack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()