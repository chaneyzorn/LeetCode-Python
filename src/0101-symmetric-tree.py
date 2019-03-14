from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.append(root)
        queue.append(root)
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if (t1 is None) and (t2 is None):
                continue
            if (t1 is None) or (t2 is None):
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def is_mirror(t1, t2):
    #         if (t1 is not None) and (t2 is not None):
    #             return True
    #         if (t1 is None) or (t2 is None):
    #             return False
    #
    #         return t1.val == t2.val \
    #                and is_mirror(t1.left, t2.right) \
    #                and is_mirror(t1.right, t2.left)
    #
    #     return is_mirror(root, root)
