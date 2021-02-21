class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parentheses_stack = list()
        s = list(s)
        for position in range(len(s)):
            rune = s[position]
            if rune == "(":
                parentheses_stack.append(position)
                continue
            if rune == ")":
                if not parentheses_stack:
                    s[position] = ""
                    continue
                parentheses_stack.pop()
        for position in parentheses_stack:
            s[position] = ""
        return "".join(s)
