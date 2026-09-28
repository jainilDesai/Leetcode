class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))  
            str_map[key].append(s)
        return list(str_map.values())