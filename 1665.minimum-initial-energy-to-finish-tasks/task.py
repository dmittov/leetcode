from typing import List
from dataclasses import dataclass

@dataclass(frozen=True)
class Task:
    cost: int
    req: int


class Solution:

    @staticmethod
    def __is_enough(tasks: List[Task], energy: int) -> bool:
        for task in tasks:
            if (task.req > energy) or (task.cost > energy):
                return False
            energy -= task.cost
        return True

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted([
            Task(cost=raw_task[0], req=raw_task[1])
            for raw_task in tasks
        ], key=lambda task: -(task.req - task.cost))
        hi = sum([task.req for task in tasks]) + 1
        lo = 0
        while (lo + 1) < hi:
            mid = (lo + hi) // 2
            if self.__is_enough(tasks, mid):
                hi = mid
            else:
                lo = mid
        if self.__is_enough(tasks, lo):
            return lo
        return hi
