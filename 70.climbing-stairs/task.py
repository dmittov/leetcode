import numpy as np


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dynamic_array = np.zeros(n, dtype=int)
        dynamic_array[0] = 1
        dynamic_array[1] = 2
        for idx in range(2, n):
            one_step = dynamic_array[idx - 1]
            two_step = dynamic_array[idx - 2]
            dynamic_array[idx] = one_step + two_step
        return dynamic_array[-1]
