"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self._add_two_numbers(l1, l2)

    def _add_two_numbers(self, l1, l2, over_bit=0):
        if not (l1 or l2):
            return over_bit and ListNode(over_bit) or None

        if l1 and l2:
            val = (l1.val + l2.val + over_bit) % 10
            over_bit = (l1.val + l2.val + over_bit) // 10
            l = ListNode(val)
            l.next = self._add_two_numbers(l1.next, l2.next, over_bit)
            return l

        if over_bit:
            return self._add_two_numbers(l1 or l2, ListNode(over_bit))
        else:
            return l1 or l2
