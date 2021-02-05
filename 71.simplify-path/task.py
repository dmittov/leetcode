class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for folder in path.split("/"):
            if not folder:
                continue
            elif folder == ".":
                continue
            elif folder == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        path = "/".join(stack)
        return f"/{path}"
