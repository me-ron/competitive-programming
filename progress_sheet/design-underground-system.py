class UndergroundSystem:

    def __init__(self):
        self.start={}
        self.end={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if self.start[id][0]+"-"+stationName not in self.end:
            self.end[self.start[id][0]+"-"+stationName]=[0,0]
        
        self.end[self.start[id][0]+"-"+stationName][0]+=(t-self.start[id][1])
        self.end[self.start[id][0]+"-"+stationName][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans=self.end[startStation+"-"+endStation][0]/self.end[startStation+"-"+endStation][1]
        return ans


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)