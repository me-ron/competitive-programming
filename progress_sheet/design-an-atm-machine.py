class ATM:

    def __init__(self):
        self.atm={20:0, 50:0, 100:0, 200:0, 500:0}
        self.notes=[500,200,100,50,20]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.atm[20]+=banknotesCount[0]
        self.atm[50]+=banknotesCount[1]
        self.atm[100]+=banknotesCount[2]
        self.atm[200]+=banknotesCount[3]
        self.atm[500]+=banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        ans=[]
        now=self.atm.copy()
        for i in self.notes:
            x=min(amount//i,now[i])
            ans.append(x)
            now[i]-=x
            amount -= (x*i)
        if not amount:
            self.atm=now
            return ans[::-1]
        return [-1]
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)