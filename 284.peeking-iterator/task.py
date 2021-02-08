# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        pass

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        pass

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        pass


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.cache = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        prev = self.cache
        if self.iter.hasNext():
            self.cache = self.iter.next()
        else:
            self.cache = None
        return prev

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].