from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = reduce(lambda x, y: x*y if y != 0 else x, nums)
        n = nums.count(0)
        x = []
        if n == 0:
            x = list(map(lambda x: int(prod/x) if x!=0 else prod, nums))
        elif n == 1:
            x = list(map(lambda x: 0 if x!=0 else prod, nums))
        else:
            x = [0]*len(nums)
        
        print(x)
        return x