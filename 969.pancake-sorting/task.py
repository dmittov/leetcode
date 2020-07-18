import numpy as np
from typing import List


class Solution:

    def max_item(self, arr):
        idx = np.argmax(arr)
        return idx, arr[idx]

    def move(self, A, idx):
        A = list(reversed(A[:idx + 1])) + A[idx + 1:]
        A = list(reversed(A))
        return A[:-1]

    def pancakeSort(self, A: List[int]) -> List[int]:
        result = self._pancakeSort(A)
        if not result:
            return None
        return result

    def _pancakeSort(self, A: List[int]):
        '''
        Not very practical task, so use convinient recursion instead of loop
        '''
        if not A:
            return []
        if len(A) == 1:
            return []
        idx, _ = self.max_item(A)
        if idx + 1 == len(A):
            return self._pancakeSort(A[:-1])
        if idx == 0:
            return [len(A)] + self._pancakeSort(list(reversed(A))[:-1])
        rest_sorting = self._pancakeSort(self.move(A, idx))
        return [idx + 1, len(A)] + (rest_sorting if rest_sorting else [])
