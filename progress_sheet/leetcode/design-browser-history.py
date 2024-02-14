class Dll:
    def __init__(self,val="",prev=None,next=None):
        self.val=val
        self.next=next
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.now=Dll(homepage)

    def visit(self, url: str) -> None:
        new_page=Dll(url,self.now)
        self.now.next=new_page
        self.now=new_page

    def back(self, steps: int) -> str:
        while steps>0 and self.now.prev:
            self.now=self.now.prev
            steps-=1
        return self.now.val

    def forward(self, steps: int) -> str:
        while steps>0 and self.now.next:
            self.now=self.now.next
            steps-=1
        return self.now.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)