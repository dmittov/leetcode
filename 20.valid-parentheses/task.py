class Solution:

    open_brackets = {'[', '(', '{'}
    matches = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    def is_open(self, c: str) -> bool:
        if c in self.open_brackets:
            return True
        return False

    def isValid(self, s: str) -> bool:
        stack = []
        for current in s:
            if self.is_open(current):
                stack.append(current)
            else:
                if not stack:
                    return False
                open_bracket = stack.pop()
                if self.matches[open_bracket] != current:
                    return False
        if stack:
            return False
        return True
