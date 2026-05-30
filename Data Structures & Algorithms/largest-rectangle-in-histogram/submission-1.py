class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [[0, heights[0]]]
        maxArea =0
        for i in range(1, len(heights)):
            minIndex = i 
            while len(stk) > 0 and stk[-1][1] > heights[i]: 
                minIndex = stk[-1][0]
                maxArea = max(maxArea, stk[-1][1] * (i - stk[-1][0] ))
                stk.pop()

            stk.append([minIndex, heights[i]]) 

        while len(stk) > 0: 
            maxArea = max(maxArea, stk[-1][1] * (len(heights) - stk[-1][0] ))
            stk.pop()

        return maxArea
        