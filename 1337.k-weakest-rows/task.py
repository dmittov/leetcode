from dataclasses import dataclass
import numpy as np
from typing import List


@dataclass(frozen=True)
class RowStrength:
    numSoldiers: int
    rowIdx: int

    def __lt__(self, other):
        return (self.numSoldiers, self.rowIdx) < (other.numSoldiers, other.rowIdx)


class Solution:
    @staticmethod
    def getRowStrength(idx: int, row: List[int]) -> RowStrength:
        numSoldiers = 0
        for item in row:
            if item == 0:
                return RowStrength(numSoldiers=numSoldiers, rowIdx=idx)
            numSoldiers += 1
        return RowStrength(numSoldiers=numSoldiers, rowIdx=idx)

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        stregths = [self.getRowStrength(idx, row) for idx, row in enumerate(mat)]
        stregths = np.partition(stregths, k - 1)
        topK = stregths[:k]
        topK.sort()
        return [rowStrength.rowIdx for rowStrength in topK]
