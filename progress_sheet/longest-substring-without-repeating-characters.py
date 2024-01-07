class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        our_set=set()
        longest = 0
        i=0
        for j in range(len(s)):
            while s[j] in our_set:
                our_set.remove(s[i])
                i+=1
            our_set.add(s[j])
            longest=max(j-i+1,longest)
        return longest
                
                
        

        