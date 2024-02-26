class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(i, s):
            if i == len(s)//2:
                return 
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            reverse(i + 1, s)
        
        reverse(0, s)
        return s
        