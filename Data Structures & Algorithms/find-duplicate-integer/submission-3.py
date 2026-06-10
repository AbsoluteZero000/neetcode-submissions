class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            print(nums, i)
            if nums[abs(i)-1] < 0:
                return abs(i)
            else:
                nums[abs(i)-1] *= -1
        
        return -9999