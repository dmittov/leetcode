import numpy as np


class DistPoint():
    def __init__(self, point):
        self.point = point
        self.distance = np.dot(point, point) ** 0.5

    def __lt__(self, other):
        return self.distance < other.distance


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == 0:
            return None
        if not points:
            return None
        wdist = np.array([DistPoint(point) for point in points])
        top_k = np.partition(wdist, K - 1)[:K]
        return [dpoint.point for dpoint in top_k]
