class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 2
        while (lo + 1) < hi:
            median = int((lo + hi) / 2)
            median_sq = median ** 2
            if median_sq > x:
                hi = median
            elif median_sq == x:
                return median
            else:
                lo = median
        return lo
