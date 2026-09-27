class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s = set()
        for i, num in enumerate(nums):
            if target - num in s:
                return [i, nums.index(target-num)]
            s.add(num)
        return [-1,-1]