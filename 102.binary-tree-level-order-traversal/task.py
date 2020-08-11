from collections import deque, defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels_dict = defaultdict(list)
        traverse_queue = deque()
        traverse_queue.append((root, 0))
        while traverse_queue:
            current_node, level = traverse_queue.popleft()
            if current_node is None:
                continue
            levels_dict[level].append(current_node.val)
            traverse_queue.append((current_node.left, level + 1))
            traverse_queue.append((current_node.right, level + 1))
        return [levels_dict[level]
                for level in sorted(list(levels_dict.keys()))]
