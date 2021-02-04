from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 0
        for min_value in counts.keys():
            max_value = min_value + 1
            length = (
                counts[min_value] + counts[max_value] if counts[max_value] > 0 else 0
            )
            best = max(best, length)
        return best
