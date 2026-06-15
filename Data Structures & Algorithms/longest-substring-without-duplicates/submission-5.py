class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
            
        i = 0
        j = 1 

        mx = 0


        while j < len(s):
            while s[j] in s[i:j]:
                i+=1
            j+=1

            mx = max(j-i, mx)
        
        return mx
            
            
            
        