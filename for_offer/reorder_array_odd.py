# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        odd, even = [], []
        for i in array:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        return odd + even
