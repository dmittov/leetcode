class Solution:
    def clear_hammingWeight(self, n: int) -> int:
        accu = 0
        while n > 0:
            accu += n % 2
            n = n >> 1  # n = n // 2
        return accu

    def fast_hammingWeight(self, n: int) -> int:
        accu = 0
        while n > 0:
            accu += 1
            n = n & (n - 1)
        return accu

    def hammingWeight(self, n: int) -> int:
        return self.fast_hammingWeight(n)
