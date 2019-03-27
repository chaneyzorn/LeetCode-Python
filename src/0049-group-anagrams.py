class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        set_record = {}
        for s in strs:
            s_set = ''.join(sorted(list(s)))
            set_record.setdefault(s_set, []).append(s)
        return set_record.values()
