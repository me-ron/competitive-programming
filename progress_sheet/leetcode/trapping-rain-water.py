class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        stack = []
    
        for i in range(len(height)):
       
            while stack and height[i] >= stack[-1][0]:
                if len(stack) > 1:
                    width = i - stack[-2][1] - 1
                    ans += width * (min(height[i], stack[-2][0]) - stack[-1][0])
                stack.pop()
            stack.append((height[i],i))

        return ans
    
