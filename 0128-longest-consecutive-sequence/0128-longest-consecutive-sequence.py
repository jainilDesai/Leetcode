class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: 
            return 0
        s = set(nums)
        length = 1
        
        for num in s:
            if num - 1 not in s:
                end = num 
                while end + 1 in s:
                    end += 1
                length = max(length, end - num + 1)
        return length
            
            