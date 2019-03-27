class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        from collections import Counter
        t_dict = Counter(tasks)
        t_list = list(t_dict.values())
        t_list.sort(reverse=True)

        imax = t_list[0] - 1
        idle_slots = imax * n

        for i in t_list[1:]:
            idle_slots -= min(imax, i)

        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
