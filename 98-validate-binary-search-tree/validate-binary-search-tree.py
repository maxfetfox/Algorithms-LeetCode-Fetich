# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BSTValidation(current, minimum, maximum):
            # если дошли до пустого узла и до этого всякий раз сохранялась последовательность, возвращаем True
            if current is None:
                return True

            # проверка, входит ли значение в диапазон (minimum – минимальное значение в поддереве, maximum – максимальное). если не входит – False. далее рекурсивно запускаем проверку в следующих поддеревьях
            return False if not minimum < current.val < maximum else BSTValidation(current.left, minimum, current.val) and BSTValidation(current.right, current.val, maximum)

        return BSTValidation(root, -2 ** 31 - 1, 2 ** 31)