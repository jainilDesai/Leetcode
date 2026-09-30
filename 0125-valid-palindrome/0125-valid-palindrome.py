class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaning all non alphanumeric chars
        #cleaned = "".join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(s) - 1
        while i < j:
            while s[i].isalnum() == False and i < j:
                i += 1 
            while s[j].isalnum() == False and i < j:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True