from dataclasses import dataclass


@dataclass(frozen=False)
class Coordinate:
    y: int
    x: int


class Solution:
    @staticmethod
    def __get_end(matrix: List[List[int]]) -> Coordinate:
        n_rows = len(matrix)
        if n_rows < 1:
            return (0, 0)
        n_cols = len(matrix[0])
        return Coordinate(y=n_rows, x=n_cols)

    @staticmethod
    def __scan(matrix: List[List[int]], end: Coordinate) -> bool:
        has_zeros_in_first_row = False
        for x in range(end.x):
            if matrix[0][x] == 0:
                has_zeros_in_first_row = True
                break
        for y in range(1, end.y):
            for x in range(end.x):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        return has_zeros_in_first_row

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        end = self.__get_end(matrix)
        if end.x < 1 or end.y < 1:
            return
        has_zeros_in_first_row = self.__scan(matrix, end)
        for y in range(1, end.y):
            if matrix[y][0] == 0:
                for x in range(end.x):
                    matrix[y][x] = 0
        for x in range(end.x):
            if matrix[0][x] == 0:
                for y in range(end.y):
                    matrix[y][x] = 0
        if has_zeros_in_first_row:
            for x in range(end.x):
                matrix[0][x] = 0
