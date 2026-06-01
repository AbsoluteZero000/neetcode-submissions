class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        total = 0

        for i in range(len(height)):
            if height[i] >= height[start]:
                for j in range(start, i):
                    total += height[start] - height[j]
                start = i


        end = len(height)-1

        for i in range(len(height) - 1, start-1, -1):
            if height[i] >= height[end]:
                for j in range(i+1, end):
                    total += height[end] - height[j]
                end = i

        return total