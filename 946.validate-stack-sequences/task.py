from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        pop_idx = 0
        push_idx = 0
        while (pop_idx < len(popped)) and (push_idx < len(pushed)):
            while pushed[push_idx] != popped[pop_idx]:
                stack.append(pushed[push_idx])
                push_idx += 1
                if push_idx >= len(pushed):
                    break
            if push_idx < len(pushed):
                stack.append(pushed[push_idx])
                push_idx += 1
            else:
                return False
            while popped[pop_idx] == stack[-1]:
                i = stack.pop()
                pop_idx += 1
                if not stack:
                    break
                if pop_idx >= len(popped):
                    break
        if pop_idx < len(popped):
            return False
        return True
