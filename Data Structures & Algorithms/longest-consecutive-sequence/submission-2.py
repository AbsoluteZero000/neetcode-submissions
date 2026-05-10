class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest_sequence_length = 0
        for i in nums:
            current_sequence_length = 0
            if i-1 not in st:
                j = i
                while j in st:
                    print(j)
                    current_sequence_length += 1
                    j += 1
            
            if longest_sequence_length < current_sequence_length:
                longest_sequence_length = current_sequence_length
            
        return longest_sequence_length
