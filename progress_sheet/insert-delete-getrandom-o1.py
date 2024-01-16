class RandomizedSet:

    def __init__(self):
        self.random=set()
        self.arr=[]
        self.dic={}
        

    def insert(self, val: int) -> bool:
        if val not in self.random:
            self.random.add(val)
            self.arr.append(val)
            self.dic[val]=len(self.arr)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.remove(val)
            self.dic[self.arr[-1]]=self.dic[val]
            self.arr[self.dic[val]],self.arr[-1]=self.arr[-1],self.arr[self.dic[val]]
            self.arr.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()