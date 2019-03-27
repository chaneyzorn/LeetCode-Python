# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def recurse(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            recurse(root.left)
            recurse(root.right)
        recurse(root)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split())

        def recurse():
            val = next(data)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = recurse()
            node.right = recurse()
            return node

        return recurse()

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     import json
    #     from collections import deque
    #
    #     res = []
    #     queue_1 = deque()
    #     queue_2 = deque()
    #     queue_1.appendleft(root)
    #
    #     while True:
    #         curr_level = []
    #         next_level = False
    #         while queue_1:
    #             node = queue_1.pop()
    #             curr_level.append(node and node.val)
    #             if node is not None:
    #                 next_level = True
    #             queue_2.appendleft(node and node.left)
    #             queue_2.appendleft(node and node.right)
    #         if not next_level:
    #             break
    #         res += curr_level
    #         queue_1, queue_2 = queue_2, queue_1
    #     return json.dumps(res)
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     import json
    #     data = data and json.loads(data)
    #     if not data:
    #         return None
    #
    #     N = len(data)
    #     curr, root = 0, TreeNode(data[0])
    #     level_1, level_2 = [root], []
    #
    #     while curr < N - 1:
    #         for node in level_1:
    #             left, right = None, None
    #             if curr + 1 <= N - 1:
    #                 left = data[curr + 1]
    #             if curr + 2 <= N - 1:
    #                 right = data[curr + 2]
    #
    #             if left is not None:
    #                 left = TreeNode(left)
    #             if right is not None:
    #                 right = TreeNode(right)
    #
    #             if node is not None:
    #                 node.left = left
    #                 node.right = right
    #
    #             level_2 += [left, right]
    #             curr += 2
    #
    #         level_1, level_2 = level_2, []
    #     return root
