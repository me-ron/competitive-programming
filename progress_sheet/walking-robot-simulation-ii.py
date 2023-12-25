class Robot:

    def __init__(self, width: int, height: int):
        self.width=width-1
        self.height=height-1
        self.dir="East"
        self.per=2*(height+width-2)
        self.mov=0
        self.pos=[0,0]

    def step(self, num: int) -> None:
        self.mov+=num
        self.mov%=self.per
        if self.mov > self.per//2 + self.width:
            self.dir = "South"
            self.pos=[0,self.height - (self.mov - (self.per//2) - self.width)]
        elif self.mov > self.per//2:
            self.dir = "West"
            self.pos=[self.width - (self.mov - (self.per//2)) ,self.height]
        elif self.mov > self.width:
            self.dir = "North"
            self.pos=[self.width, self.mov - self.width ]
        elif not self.mov:
            self.dir = "South"
            self.pos=[0,0]
        else:
            self.dir = "East"
            self.pos=[self.mov,0]
            

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir
        
    
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()