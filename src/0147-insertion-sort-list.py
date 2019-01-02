"""
Sort a linked list using insertion sort.

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = dummy = ListNode(0)
        curr = prev.next = head
        while curr and curr.next:
            next_val = curr.next.val  # find one to relocate
            if curr.val <= next_val:
                curr = curr.next
            else:  # curr.val > next_val
                if prev.next.val > next_val:
                    prev = dummy  # go back to head
                while prev.next.val <= next_val:
                    prev = prev.next

                node = curr.next
                curr.next = node.next
                node.next = prev.next
                prev.next = node
        return dummy.next

    # def insertionSortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head:
    #         return
    #
    #     in_list = head.next
    #     out_list = head
    #     out_list.next = None
    #     while in_list:
    #         next = in_list.next
    #         out_list = self.insert_one(out_list, in_list)
    #         in_list = next
    #     return out_list
    #
    # def insert_one(self, head, node):
    #     p1, p2 = head, head.next
    #     if node.val < p1.val:
    #         node.next = p1
    #         return node
    #
    #     while p2 and node.val > p2.val:
    #         p1, p2 = p2, p2.next
    #
    #     p1.next = node
    #     node.next = p2
    #     return head
