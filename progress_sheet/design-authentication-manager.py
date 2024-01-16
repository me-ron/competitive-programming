class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tolive=timeToLive
        self.dic={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId]=currentTime + self.tolive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic and self.dic[tokenId]>currentTime:
            self.dic[tokenId]=currentTime + self.tolive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans=0
        for i in self.dic:
            ans+=(self.dic[i]>currentTime)
        return ans


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)