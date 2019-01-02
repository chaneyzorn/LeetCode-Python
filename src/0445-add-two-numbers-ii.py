"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        jump_count = 0

        while True:
            p1 = p1.next
            p2 = p2.next
            if not p1:
                p1 = l2
                jump_count += 1
                if jump_count == 2:
                    long, short = l1, l2
                    start, stop = p1, p2
            if not p2:
                p2 = l1
                jump_count += 1
                if jump_count == 2:
                    long, short = l2, l1
                    start, stop = p2, p1
            if jump_count == 2:
                break

        over_bit = self._add_two(start, stop)
        if over_bit == 0:
            return long
        over_bit = self._add_long(long, stop, over_bit)
        if over_bit == 0:
            return long
        head = ListNode(over_bit)
        head.next = long
        return head

    def _add_two(self, p1, p2):
        if not (p1 and p2):
            return 0
        val = p1.val + p2.val + self._add_two(p1.next, p2.next)

        over_bit = 0
        if val >= 10:
            over_bit = 1
            val -= 10
        p2.val = val
        return over_bit

    def _add_long(self, long, stop, over_bit):
        if long is stop:
            return over_bit
        val = long.val + self._add_long(long.next, stop, over_bit)

        over_bit = 0
        if val >= 10:
            over_bit = 1
            val -= 10
        long.val = val
        return over_bit
