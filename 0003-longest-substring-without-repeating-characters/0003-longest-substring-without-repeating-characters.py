class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        max_len = 1
        left = 0
        right = left + 1
        window = {s[left]}
        while right < len(s):
            while right < len(s) and s[right] in window:
                window.remove(s[left])
                left = left + 1
            window.add(s[right])
            right = right + 1
            max_len = max(max_len, len(window))
        return max_len

            