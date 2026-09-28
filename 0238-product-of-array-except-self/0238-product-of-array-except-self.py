class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        left, right = [1] * length, [1] * length
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        result = [0] * length
        for i in range(length):
            result[i] = left[i] * right[i]
        return result