# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def get_left_most_right(node):
            most_right = node.left
            while most_right.right and most_right.right is not node:
                most_right = most_right.right
            return most_right

        cur, result = root, []
        while cur:
            if not cur.left:
                result.append(cur.val)
                cur = cur.right
            else:
                most_right = get_left_most_right(cur)
                if not most_right.right:
                    most_right.right = cur
                    cur = cur.left
                else:
                    most_right.right = None
                    result.append(cur.val)
                    cur = cur.right
        return result

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     cur, stack, result = root, [], []
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #         cur = stack.pop()
    #         result.append(cur.val)
    #         cur = cur.right
    #     return result

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     result = []
    #
    #     def in_order(root):
    #         if not root:
    #             return
    #         in_order(root.left)
    #         result.append(root.val)
    #         in_order(root.right)
    #
    #     in_order(root)
    #     return result
