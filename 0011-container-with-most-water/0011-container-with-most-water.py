class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            current_space = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, current_space)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area