class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}
        for ch in s:
            if ch in sMap:
                sMap[ch] += 1
            else: 
                sMap[ch] = 1
        for ch in t:
            if ch in tMap:
                tMap[ch] += 1
            else:
                tMap[ch] = 1
        return sMap == tMap
            