class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "".join((str(len(st)) + '#' + st) for st in strs)
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            temp = ""
            while(i < len(s) and s[i] != '#'):
                temp += s[i]
                i+=1
            siz = int(temp)
            temp = ""
            for j in range(siz):
                temp += s[i+j+1]
            
            res.append(temp)
            i += siz+1
        return res


        

