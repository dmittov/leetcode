from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GraphNode:
    node: int
    part: int


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        unchecked = set(range(len(graph)))
        while unchecked:
            start_node = next(iter(unchecked))
            queue = deque([GraphNode(start_node, 0)])
            seen = set()
            part_mapping = dict()
            while queue:
                current = queue.popleft()
                if current.node in seen:
                    if current.part != part_mapping[current.node]:
                        return False
                    continue
                part_mapping[current.node] = current.part
                seen.add(current.node)
                assign_part = (current.part + 1) % 2
                for neighbor in graph[current.node]:
                    if neighbor in seen:
                        continue
                    queue.append(GraphNode(neighbor, assign_part))
            unchecked -= seen
        return True
