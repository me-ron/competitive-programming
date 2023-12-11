class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lst2={st:i for i,st in enumerate(list2)}
        lst1={st:i for i,st in enumerate(list1)}
        m=len(list1)+len(list2)-2
        for i in lst2:
            if i in lst1:
                m=min(lst1[i]+lst2[i],m)
                lst2[i]+=lst1[i]
            else:
                list2.remove(i)
        return [i for i in list2 if lst2[i]==m]