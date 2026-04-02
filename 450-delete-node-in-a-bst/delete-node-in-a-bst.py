# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def BSTDel(current, value=key):
            if current is None:
                return None

            if value < current.val:
                current.left = BSTDel(current.left, value)

            elif value > current.val:
                current.right = BSTDel(current.right, value)

            else:
                left = current.left
                right = current.right

                if left is None and right is None:
                    return None

                elif left is None:
                    return right

                elif right is None:
                    return left

                else:
                    successor = right
                    while successor.left is not None:
                        successor = successor.left

                    current.val = successor.val
                    current.right = BSTDel(current.right, current.val)
            return current
        return BSTDel(root, key)