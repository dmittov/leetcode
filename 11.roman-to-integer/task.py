class Solution:

    symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        prev = 0
        total = 0
        for symbol in s:
            symbol_value = self.symbols[symbol]
            if symbol_value > prev:
                total -= 2 * prev
            total += symbol_value
            prev = symbol_value
        return total
