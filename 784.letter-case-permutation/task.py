from collections import deque
from typing import List


class Solution:
    def simpleRecursion(self, S: str) -> List[str]:
        for position in range(len(S)):
            symbol = S[position]
            if symbol.upper() == symbol.lower():
                continue
            prefix = S[:position]
            lower_part = [
                f"{prefix}{symbol.lower()}{postfix}"
                for postfix in self.letterCasePermutation(S[position + 1 :])
            ]
            upper_part = [
                f"{prefix}{symbol.upper()}{postfix}"
                for postfix in self.letterCasePermutation(S[position + 1 :])
            ]
            return lower_part + upper_part

    def letterCasePermutation(self, S: str) -> List[str]:
        queue = deque([(0, S)])
        answer = []
        sz = len(S)
        while queue:
            position, option_s = queue.popleft()
            if position == sz:
                answer.append(option_s)
                continue
            symbol = option_s[position]
            if symbol.upper() == symbol.lower():
                queue.append((position + 1, option_s))
            else:
                upper_option = (
                    position + 1,
                    f"{option_s[:position]}{symbol.upper()}{option_s[position + 1:]}",
                )
                lower_option = (
                    position + 1,
                    f"{option_s[:position]}{symbol.lower()}{option_s[position + 1:]}",
                )
                queue.append(upper_option)
                queue.append(lower_option)
        return answer
