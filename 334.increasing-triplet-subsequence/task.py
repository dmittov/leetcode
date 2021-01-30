class Solution:
    @staticmethod
    def __increasing_k(nums: List[int], k: int) -> bool:
        best = [nums[0]]
        for num in nums[1:]:
            location = None
            for idx, value in enumerate(best):
                if num <= value:
                    location = idx
                    best[idx] = num
                    break
            if location is None:
                best.append(num)
            if len(best) >= k:
                return True
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.__increasing_k(nums, 3)
