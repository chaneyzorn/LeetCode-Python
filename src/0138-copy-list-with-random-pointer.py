"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        curr = head
        while curr:  # A -> A' -> B -> B' -> C -> C'
            copy_node = RandomListNode(curr.label)
            copy_node.random = curr.random

            copy_node.next = curr.next
            curr.next = copy_node
            curr = copy_node.next

        copy_node = head.next
        while copy_node:
            copy_node.random = copy_node.random and copy_node.random.next
            copy_node = copy_node.next and copy_node.next.next

        old_curr, new_curr, new_list = head, head.next, head.next
        while old_curr and new_curr:
            old_curr.next = new_curr.next
            new_curr.next = new_curr.next and new_curr.next.next

            old_curr = old_curr.next
            new_curr = new_curr.next

        return new_list

    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     if not head:
    #         return head
    #
    #     curr = head
    #     copy_dict = {curr: RandomListNode(curr.label)}
    #     while curr:
    #         if curr.next:
    #             if curr.next not in copy_dict:
    #                 copy_dict[curr.next] = RandomListNode(curr.next.label)
    #             copy_dict[curr].next = copy_dict[curr.next]
    #         if curr.random:
    #             if curr.random not in copy_dict:
    #                 copy_dict[curr.random] = RandomListNode(curr.random.label)
    #             copy_dict[curr].random = copy_dict[curr.random]
    #
    #         curr = curr.next
    #
    #     return copy_dict[head]

    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     if not head:
    #         return head
    #
    #     copy_dict = {}
    #     copy_list = dummy = RandomListNode(0)
    #     curr = head
    #     while curr:
    #         node = RandomListNode(curr.label)
    #         node.random = curr.random
    #         copy_dict[curr] = node
    #
    #         copy_list.next = node
    #         copy_list = copy_list.next
    #
    #         curr = curr.next
    #
    #     curr = dummy.next
    #     while curr:
    #         curr.random = curr.random and copy_dict[curr.random]
    #         curr = curr.next
    #     return dummy.next
