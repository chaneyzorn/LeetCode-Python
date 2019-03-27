class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = {i: [] for i in range(numCourses)}
        for from_node, to_node in prerequisites:
            adj[from_node].append(to_node)

        state = [0] * numCourses

        def can_take(node):
            if state[node] in (-1, 1):
                return state[node] == 1
            state[node] = -1
            if any(not can_take(j) for j in adj[node]):
                return False
            state[node] = 1
            return True

        return all(can_take(node) for node in range(numCourses))

    # def canFinish(self, numCourses, prerequisites):
    #     """
    #     :type numCourses: int
    #     :type prerequisites: List[List[int]]
    #     :rtype: bool
    #     """
    #     # 邻接表
    #     adj = {i: [] for i in range(numCourses)}
    #     # 入度表
    #     in_degree = {i: 0 for i in range(numCourses)}
    #
    #     for from_node, in_node in prerequisites:
    #         in_degree[in_node] += 1
    #         adj.get(from_node).append(in_node)
    #
    #     from collections import deque
    #     zero_degree = deque()  # 零入度队列
    #     for key, val in in_degree.items():
    #         if val == 0:
    #             zero_degree.appendleft(key)
    #
    #     counter = 0  # 拓扑排序
    #     while zero_degree:
    #         from_node = zero_degree.pop()
    #         counter += 1
    #
    #         for in_node in adj.get(from_node):
    #             in_degree[in_node] -= 1
    #             if in_degree[in_node] == 0:
    #                 zero_degree.appendleft(in_node)
    #     return counter == numCourses  # 如果不能完成拓扑排序，则有环
