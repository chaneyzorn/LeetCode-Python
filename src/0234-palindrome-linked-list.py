"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        curr = None
        slow, fast = head, head.next
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = curr
            curr = temp

        l1 = slow.next
        if fast:  # even
            slow.next = curr
            l2 = slow
        else:  # odd
            l2 = curr

        while l1:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
