class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(arr, l, r, player1):
            if r - l == 0:
                return arr[l]

            if player1:
                left = arr[l] + score(arr, l + 1, r, 0)
                right = arr[r] + score(arr, l, r - 1, 0)
                return max(left,right)
                
            else:
                left = score(arr, l + 1, r, 1)
                right = score(arr, l, r - 1, 1) 
                return min(left, right)

        player1 = score(nums, 0, len(nums) - 1, 1)
        player2 = sum(nums) - player1
        return player1 >= player2 
