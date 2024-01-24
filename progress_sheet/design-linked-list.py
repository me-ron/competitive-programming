class node:
    def __init__(self,value):
        self.val=value
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=node(0)
        self.size=0

    def get(self, index: int) -> int:
        temp= self.head.next
        for i in range(index):
            if temp==None:
                return -1
            temp=temp.next
        return temp.val if self.size>index else -1

    def addAtHead(self, val: int) -> None:
        x=node(val)
        x.next=self.head.next
        self.head.next=x
        self.size+=1

    def addAtTail(self, val: int) -> None:
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=node(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size<index:
            return
        x=node(val)
        temp=self.head
        i=0
        while i<index and temp.next:
            temp=temp.next
            i+=1 
        x.next=temp.next
        temp.next=x
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if self.size<=index:
            return
        temp=self.head
        i=0
        while i<index and temp.next:
            temp=temp.next
            i+=1 
        if temp.next:
            temp.next=temp.next.next
        self.size-=1
