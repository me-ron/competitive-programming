class FrequencyTracker:

    def __init__(self):
        self.freq={}
        self.r_freq=defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.freq :
            self.r_freq[self.freq[number]]-= (self.r_freq[self.freq[number]]!=0)
            self.freq[number]+=1
        else:
            self.freq[number]=1
        self.r_freq[self.freq[number]]+=1


    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.r_freq[self.freq[number]]-= (self.r_freq[self.freq[number]]!=0)
            self.freq[number]-=1
            if self.freq[number]==0:
                self.freq.pop(number)
            else:
                self.r_freq[self.freq[number]]+=1
                  
    def hasFrequency(self, frequency: int) -> bool:
        return bool(self.r_freq[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)