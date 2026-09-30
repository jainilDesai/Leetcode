class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaning all non alphanumeric chars
        #cleaned = "".join(char.lower() for char in s if char.isalnum())
        lower_s = s.lower()
        i, j = 0, len(lower_s) - 1
        while i < j:
            while lower_s[i].isalnum() == False and i < j:
                i += 1 
            while lower_s[j].isalnum() == False and i < j:
                j -= 1
            if lower_s[i] == lower_s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True