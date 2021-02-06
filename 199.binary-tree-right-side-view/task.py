from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        level_most_right = {}
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            level_most_right[level] = node.val
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        right_side_view = [
            level_most_right[level] for level in range(len(level_most_right))
        ]
        return right_side_view
