from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for value in strs:
            key = str(sorted(value))
            str_dict[key].append(value)
        return list(str_dict.values())
