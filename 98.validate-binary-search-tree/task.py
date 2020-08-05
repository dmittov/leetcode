# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def __is_valid_bst(self, root: TreeNode, possible_min, possible_max) -> bool:
        if root is None:
            return True
        if possible_min and possible_min >= root.val:
            return False
        if possible_max and possible_max <= root.val:
            return False
        if root.left and (root.val <= root.left.val):
            return False
        if root.right and (root.val >= root.right.val):
            return False
        is_left_valid =  self.__is_valid_bst(root.left, possible_min, root.val)
        is_right_valid =  self.__is_valid_bst(root.right, root.val, possible_max)
        return is_left_valid and is_right_valid
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.__is_valid_bst(root, None, None)
        