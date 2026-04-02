# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def BSTInsertion(current, value):
            if current.val < value:
                if current.right is None:
                    current.right = TreeNode(value)
                else:
                    return BSTInsertion(current.right, value)
            elif current.val > value:
                if current.left is None:
                    current.left = TreeNode(value)
                else:
                    return BSTInsertion(current.left, value)
        BSTInsertion(root, val)
        return root