# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BSTValidation(current, minimum, maximum):
            if current is None:
                return True

            return False if not minimum < current.val < maximum else BSTValidation(current.left, minimum, current.val) and BSTValidation(current.right, current.val, maximum)

        return BSTValidation(root, -2 ** 31 - 1, 2 ** 31)