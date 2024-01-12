class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket=defaultdict(int)
        i=0
        ans=0
        for j in range(len(fruits)):
            basket[fruits[j]]+=1
            while len(basket)>2:
                basket[fruits[i]]-=1
                if basket[fruits[i]]==0:
                    basket.pop(fruits[i])
                i+=1
            ans=max(ans,j-i+1)
        return ans
        
        