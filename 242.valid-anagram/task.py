from collections import Counter


class Solution:
    def __sortingCheck(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False

    def __hashCheck(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        for symbol in t:
            s_dict[symbol] -= 1
            if s_dict[symbol] < 0:
                return False
        if s_dict and max(s_dict.values()) > 0:
            return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return self.__hashCheck(s, t)
