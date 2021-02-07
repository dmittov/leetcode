import heapq
from typing import List


class Solution:
    def _graphShortestToChar(self, s: str, c: str) -> List[int]:
        seen = set()
        priority_queue = []
        distances = []
        sz = len(s)
        for idx, rune in enumerate(s):
            if rune == c:
                heapq.heappush(priority_queue, (0, idx))
            distances.append(sz)
        while priority_queue:
            distance, idx = heapq.heappop(priority_queue)
            if (idx < 0) or (idx >= len(s)) or (idx in seen):
                continue
            distances[idx] = distance
            seen.add(idx)
            heapq.heappush(priority_queue, (distance + 1, idx + 1))
            heapq.heappush(priority_queue, (distance + 1, idx - 1))
        return distances

    def _twoPassShortestToChar(self, s: str, c: str) -> List[int]:
        distances = []
        closest_idx = -len(s)
        # forward pass
        for idx, rune in enumerate(s):
            if rune == c:
                closest_idx = idx
            distances.append(idx - closest_idx)
        # backward pass
        closest_idx = 2 * len(s)
        for rev_idx, rune in enumerate(s[::-1]):
            idx = len(s) - rev_idx - 1
            if rune == c:
                closest_idx = idx
            right_distance = closest_idx - idx
            distances[idx] = min(distances[idx], right_distance)
        return distances

        def shortestToChar(self, s: str, c: str) -> List[int]:
            return self._twoPassShortestToChar(s, c)
