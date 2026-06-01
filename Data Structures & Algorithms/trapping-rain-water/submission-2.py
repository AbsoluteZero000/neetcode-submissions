class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        total = 0
        currTotal = 0

        for i in range(len(height)):
            if height[i] >= height[start]:
                total += currTotal
                start = i
                currTotal = 0
            else:
                currTotal += height[start] - height[i]


        start = len(height) - 1
        currTotal = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > height[start]:
                total += currTotal
                start = i
                currTotal = 0
            else:
                currTotal += height[start] - height[i]
        return total