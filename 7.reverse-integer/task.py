class Solution:

    def __is_overflow(self, x):
        return not (-2 ** 31 <= x <= 2 ** 31 - 1)

    def reverse(self, x: int) -> int:
        if x >= 0:
            return self.__reversed(x)
        return - self.__reversed(-x)

    def __reversed(self, x: int) -> int:
        reversed_str = "".join(reversed(str(x))).lstrip("0")
        if reversed_str == "":
            reversed_str = "0"
        result = int(reversed_str)
        if self.__is_overflow(result):
            return 0
        return result
