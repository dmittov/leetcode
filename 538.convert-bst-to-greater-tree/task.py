# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        accu = 0

        def traverse(root: TreeNode):
            if root is None:
                return None
            nonlocal accu
            traverse(root.right)
            accu += root.val
            root.val = accu
            traverse(root.left)

        traverse(root)
        return root
