class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return [[""]]
        str_map = {}
        for str in strs:
            temp = "".join(sorted(str))
            if temp not in str_map:
                str_map[temp] = []   
            str_map[temp].append(str)
        return list(str_map.values())