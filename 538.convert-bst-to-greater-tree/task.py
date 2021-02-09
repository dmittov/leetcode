# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __convert(self, root: TreeNode, tval: int) -> TreeNode:
        if root is None:
            return None, 0
        rtree, rval = self.__convert(root.right, tval)
        root.val += tval if rtree is None else rval
        ltree, lval = self.__convert(root.left, root.val)
        return root, root.val if ltree is None else lval

    def convertBST(self, root: TreeNode) -> TreeNode:
        root, val = self.__convert(root, 0)
        return root
