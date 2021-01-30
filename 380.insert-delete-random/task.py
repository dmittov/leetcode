import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__locations = dict()
        self.__storage = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.__locations:
            return False
        self.__storage.append(val)
        self.__locations[val] = len(self.__storage) - 1
        return True

    def __exchange(self, lhs: int, rhs: int):
        (self.__locations[lhs], self.__locations[rhs]) = (
            self.__locations[rhs],
            self.__locations[lhs],
        )
        self.__storage[self.__locations[lhs]] = lhs
        self.__storage[self.__locations[rhs]] = rhs

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.__storage:
            return False
        self.__exchange(val, self.__storage[-1])
        self.__storage.pop()
        del self.__locations[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.__storage)
