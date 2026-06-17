class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 ="".join(sorted(s1))
        i = 0
        j = len(s1)

        while j < len(s2)+1:
            if s1 in "".join(sorted(s2[i:j])):
                return True
            j+=1
            i+=1
        return False