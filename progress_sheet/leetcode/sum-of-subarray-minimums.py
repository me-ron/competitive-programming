
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        ans = [0] *len(arr)
        stack = [0]

        for i in range(1,len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1]
            ans[i] = ans[j] + (i - j) * arr[i]
            stack.append(i)
        
        return sum(ans) % (10**9 + 7)