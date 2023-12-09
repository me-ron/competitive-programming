class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic={}
        for i in matches:
            if i[0] not in dic:
                dic[i[0]]=0
            if i[1] not in dic:
                dic[i[1]]=1
            else:
                dic[i[1]]+=1

        dic={key:value for key,value in sorted(dic.items(),key= lambda x:x[0])}

        ans=[[],[]]
        for i in dic:
            if dic[i]==0:
                ans[0].append(i)
            elif dic[i]==1:
                ans[1].append(i)
        return ans
        