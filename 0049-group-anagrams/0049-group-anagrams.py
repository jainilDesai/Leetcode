class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            str_map[key].append(s)
        return list(str_map.values())