class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(cleaned) - 1
        while i < j:
            if cleaned[i] == cleaned[j]:
                i += 1
                j -= 1
            else:
                return False
        return True