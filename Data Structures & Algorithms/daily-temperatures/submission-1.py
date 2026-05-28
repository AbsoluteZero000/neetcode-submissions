class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            while( len(stk) > 0 and stk[-1][1] <= temperatures[i]):
                stk.pop()
            
            
            if(len(stk) <= 0):
                res.append(0)
            else:
                res.append(stk[-1][0] - i) 

            stk.append([i, temperatures[i]])

        res.reverse()
        return res
