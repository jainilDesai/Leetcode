class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = {}
        for i, num in enumerate(nums):
            if target - num in s:
                return [s[target-num], i]
            s[num] = i
        return [-1,-1]