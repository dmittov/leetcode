from typing import List, Iterator
from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Coordinate:
    y: int
    x: int

        
class Grid:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.sz = len(grid)
        assert self.sz > 0
        assert len(grid[0]) ==self. sz
        
    def isValid(self, point: Coordinate) -> bool:
        if (point.y < 0) or (point.x < 0):
            return False
        if (point.y >= self.sz) or (point.x >= self.sz):
            return False
        return True
    
    def isEmpty(self, point: Coordinate) -> bool:
        if self.grid[point.y][point.x] == 0:
            return True
        return False
    
    def getNeighbors(self, point: Coordinate) -> Iterator[Coordinate]:
        for diff_y in [-1, 0, 1]:
            for diff_x in [-1, 0, 1]:
                if (diff_x == 0) and (diff_y == 0):
                    continue
                neighbor = Coordinate(y = point.y + diff_y, x = point.x + diff_x)
                if self.isValid(neighbor) and self.isEmpty(neighbor):
                    yield neighbor


class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        grid = Grid(grid)
        distances = [[None for x in range(grid.sz)]for y in range(grid.sz)]
        seen = [[False for x in range(grid.sz)]for y in range(grid.sz)]
        start = Coordinate(0, 0)
        finish = Coordinate(grid.sz - 1, grid.sz - 1)
        queue = deque()
        if grid.isEmpty(start) and grid.isEmpty(finish):
            queue.append(start)
            seen[start.y][start.x] = True
            distances[start.y][start.x] = 1
        while queue:
            current = queue.popleft()            
            for neighbor in grid.getNeighbors(current):
                if not seen[neighbor.y][neighbor.x]:
                    distances[neighbor.y][neighbor.x] = distances[current.y][current.x] + 1
                    seen[neighbor.y][neighbor.x] = True
                    queue.append(neighbor)
        return -1 if distances[finish.y][finish.x] is None else distances[finish.y][finish.x]
