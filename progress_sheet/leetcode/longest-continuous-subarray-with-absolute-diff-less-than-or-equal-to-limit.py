class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        MIN = deque()
        MAX = deque()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while MAX and nums[MAX[-1]] < nums[r]:
                MAX.pop()
            while MIN and nums[MIN[-1]] > nums[r]:
                MIN.pop()
            MAX.append(r)
            MIN.append(r)

            abs_diff = nums[MAX[0]] - nums[MIN[0]]
            while abs_diff > limit and MIN and MAX:
                if MIN[0] == l:
                    MIN.popleft()
                if MAX[0] == l:
                    MAX.popleft()
                l += 1
                abs_diff = nums[MAX[0]] - nums[MIN[0]]

            ans = max(r - l + 1, ans)
        return ans