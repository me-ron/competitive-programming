class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.arr = [-1] * k
        self.front = 0
        self.rear = -1
        self.size = 0 
    
    def isEmpty(self) -> bool:
        return not self.size 

    def isFull(self) -> bool:
        return self.size == self.k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.k
        self.arr[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.arr[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.arr[self.front]

    def Rear(self) -> int:
        return self.arr[self.rear]


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()