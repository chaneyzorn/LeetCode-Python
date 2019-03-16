# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def convert(p):
            result = "^"
            if p:
                result += str(p.val) + "#" + convert(p.left) + convert(p.right)
            result += "$"
            return result

        return convert(t) in convert(s)

    # def isSubtree(self, s, t):
    #     """
    #     :type s: TreeNode
    #     :type t: TreeNode
    #     :rtype: bool
    #     """
    #     if not s:
    #         return False
    #     return self.is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    #
    # def is_same(self, t1, t2):
    #     if (t1 is None) and (t2 is None):
    #         return True
    #     if (t1 is None) or (t2 is None):
    #         return False
    #     if t1.val != t2.val:
    #         return False
    #     return self.is_same(t1.left, t2.left) and self.is_same(t1.right, t2.right)
