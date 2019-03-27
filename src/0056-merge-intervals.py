# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        res = []
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        for curr in intervals[1:]:
            if curr.start <= prev.end:
                prev.start, prev.end = prev.start, max(prev.end, curr.end)
            else:
                res.append(prev)
                prev = curr
        res.append(prev)
        return res
