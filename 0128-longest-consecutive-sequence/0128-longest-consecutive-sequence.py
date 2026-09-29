class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums: 
            return 0
        s = set(nums)
        length = 1
        
        for num in s:
            current = 1
            if num - 1 not in s:
                while num + 1 in s:
                    current += 1
                    num = num + 1
            length = max(length, current)
        return max(length, current)
            
            