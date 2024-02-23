class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        n = len(nums)
        ans = [0] * (n - k + 1)
        l = 0
        for r in range(n):
            if r - l + 1 > k:
                l += 1
            if queue and queue[0] < l:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            ans[l] = nums[queue[0]]

        return ans
        