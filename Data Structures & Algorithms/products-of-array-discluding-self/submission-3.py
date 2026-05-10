from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i-1]*res[i-1]
        print(res)
        pos = 1
        for i in range(len(nums)-1, 0, -1):
            pos *= nums[i]
            print("pos = " + str(pos))
            res[i-1] *= pos
        print(res)
        
        return res

