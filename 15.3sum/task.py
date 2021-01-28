from collections import Counter


class Solution:
    @staticmethod
    def __check(storage: Counter, used: Counter):
        for num, usage_count in used.items():
            if storage[num] < usage_count:
                return False
        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        target = 0
        storage = Counter(nums)
        keys = list(storage.keys())
        for left_idx in range(len(keys)):
            for right_idx in range(left_idx, len(keys)):
                left = keys[left_idx]
                right = keys[right_idx]
                rest = target - left - right
                if storage[rest] < 1:
                    continue
                candidates = sorted([left, right, rest])
                if self.__check(storage, Counter(candidates)):
                    results.add(tuple(candidates))
        return [list(tup) for tup in sorted(results)]
