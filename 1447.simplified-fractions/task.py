from typing import List


class Solution:
    def gcd(self, grt: int, lst: int):
        while lst != 0:
            grt, lst = lst, grt % lst
        return grt
            
    def simplifiedFractions(self, n: int) -> List[str]:
        solution = set()
        for divisor in range(2, n + 1):
            for divident in range(1, divisor):
                gcd = self.gcd(divisor, divident)
                fraction = f"{int(divident / gcd)}/{int(divisor / gcd)}"
                solution.add(fraction)
        return list(solution)
