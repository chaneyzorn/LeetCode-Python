# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque()
        queue.appendleft(root)
        queue2 = deque()
        result = []
        while queue:
            item = []
            while queue:
                node = queue.pop()
                item.append(node.val)
                if node.left:
                    queue2.appendleft(node.left)
                if node.right:
                    queue2.appendleft(node.right)
            if item:
                result.append(item)
            queue, queue2 = queue2, queue
        return result
