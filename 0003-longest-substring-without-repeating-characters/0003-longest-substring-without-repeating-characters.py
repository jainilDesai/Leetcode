class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left = left + 1
            window.add(s[right])
            max_len = max(max_len, len(window))
        return max_len

            