from typing import List


class Solution:
    @staticmethod
    def rle(lst: List[int]) -> List[int]:
        prev = None
        length = 0
        result = list()
        for current in lst:
            if current == prev:
                length += 1
            else:
                result.append(length)
                length = 1
            prev = current
        result.append(length)
        return result

    @staticmethod
    def count_seq(rle_value: int) -> int:
        if rle_value < 2:
            return 0
        return rle_value * (rle_value - 1) // 2

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        diff = [p - q for p, q in zip(A, A[1:])]
        rle = self.rle(diff)
        return sum(self.count_seq(rle_val) for rle_val in rle)
