class Solution:
    def isHappy_with_set(self, n: int) -> bool:
        observed = {n}
        while n != 1:
            digits = [int(s) for s in str(n)]
            n = sum(digit ** 2 for digit in digits)
            if n in observed:
                return False
            observed.add(n)
        return True

    @staticmethod
    def transform(n: int) -> int:
        digits = list()
        while n > 0:
            n, digit = n // 10, n % 10
            if digit > 0:
                digits.append(digit)
        return sum(digit ** 2 for digit in digits)

    def isHappy(self, n: int) -> bool:
        slow_ptr = self.transform(n)
        fast_ptr = self.transform(self.transform(n))
        while slow_ptr != fast_ptr:
            slow_ptr = self.transform(slow_ptr)
            fast_ptr = self.transform(self.transform(fast_ptr))
        if slow_ptr == 1:
            return True
        return False
