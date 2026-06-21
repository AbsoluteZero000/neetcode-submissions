class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) * len(matrix[0]) -1 

        while j >= i:
            mid = i + (j-i)//2
            midVal = matrix[mid//len(matrix[0])][mid%len(matrix[0])] 
            if midVal > target:
                j = mid -1
            elif midVal < target:
                i = mid + 1
            else:
                return True
        return False
        
            