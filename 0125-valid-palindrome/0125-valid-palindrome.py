class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaning all non alphanumeric chars
        #cleaned = "".join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1 
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True