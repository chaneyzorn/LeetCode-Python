# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack, limit = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= limit:
                return False
            limit = root.val
            root = root.right
        return True

    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     self.min = float('-inf')
    #
    #     def valid(root):
    #         if not root:
    #             return True
    #
    #         if not valid(root.left):
    #             return False
    #
    #         if root.val <= self.min:
    #             return False
    #         self.min = root.val
    #
    #         if not valid(root.right):
    #             return False
    #         return True
    #
    #     return valid(root)
