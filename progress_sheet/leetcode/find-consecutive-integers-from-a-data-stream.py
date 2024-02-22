class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.unique = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.unique[num] += 1

        if len(self.queue) > self.k:
            self.unique[self.queue[0]] -= 1
            if self.unique[self.queue[0]] == 0:
                self.unique.pop(self.queue[0])
            self.queue.popleft()
        
        return len(self.unique) == 1 and len(self.queue) == self.k and self.queue[0] == self.value

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)