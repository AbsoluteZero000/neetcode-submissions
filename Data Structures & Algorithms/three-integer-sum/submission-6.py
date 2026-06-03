class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set() 
        nums.sort()
        for k in range(1, len(nums)-1):
            i = 0 
            j = len(nums)-1  
            while i < k and j > k:
                if nums[i] + nums[j] + nums[k] > 0:
                    j-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i+=1
                else:
                    res.add(tuple([nums[i],nums[k],nums[j]]))
                    j-=1

        return list(res)
        