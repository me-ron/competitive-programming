class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        small = nums[-1]
        n = len(nums)
        ans = 0
        for i in range(n-2, -1, -1):

            if nums[i] > small:
                ans += (nums[i] // small) if nums[i] % small else (nums[i] // small - 1)
                small = small if not nums[i] % small else nums[i]//(nums[i]//small + 1)
            else:
                small = nums[i]

        return ans