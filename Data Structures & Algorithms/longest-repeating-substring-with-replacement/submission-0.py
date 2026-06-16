from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1

        res = 0
        while j <= len(s):
            frequencies = Counter(s[i:j])
            print(frequencies, i, j)
            mx = 0
            cnt =0 
            for key in frequencies:
                cnt += frequencies.get(key)
                mx = max(mx, frequencies.get(key))
            
            cnt -= mx 

            if cnt > k:
                i+= 1
                continue

            res = max(res, j-i)
            j+=1
        return res

