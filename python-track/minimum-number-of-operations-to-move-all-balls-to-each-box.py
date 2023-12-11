class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes=list(boxes)
        lst=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                lst.append(i)
        for i in range(len(boxes)):
            sum=0
            for j in range(len(lst)):
                sum+=abs(i-lst[j])
            boxes[i]=sum 
        return boxes

        