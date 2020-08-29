from typing import Iterable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    pre_idx = 0

    @staticmethod
    def _find(inorder: List[int], value: int, idx_it: Iterable[int]) -> int:
        for idx in idx_it:
            if inorder[idx] == value:
                return idx

    def _build_tree(self,
                    preorder: List[int], inorder: List[int],
                    begin_idx: int, end_idx: int) -> TreeNode:
        if begin_idx > end_idx:
            return None
        value = preorder[self.pre_idx]
        self.pre_idx += 1
        if begin_idx == end_idx:
            return TreeNode(value, None, None)
        idx = self._find(inorder, value, range(begin_idx, end_idx + 1))
        left_node = self._build_tree(preorder, inorder, begin_idx, idx - 1)
        right_node = self._build_tree(preorder, inorder, idx + 1, end_idx)
        return TreeNode(value, left_node, right_node)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build_tree(preorder, inorder, 0, len(inorder) - 1)
