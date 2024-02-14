class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=ten=0
        for i in bills:
            if i==20:
                if five and ten:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
            elif i==10:
                if not five:
                    return False
                five-=1
                ten+=1
            else:
                five+=1
        return True