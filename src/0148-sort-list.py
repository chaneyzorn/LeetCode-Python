"""
Sort a linked list in O(n log n) time using constant space complexity.

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

    def __str__(self):
        curr = self
        values = []
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return "->".join(values)


class Solution(object):
    def sortList(self, head):
        """
        merge sort with recursion
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        if not l2:
            return head

        l1 = self.sortList(head)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


"""
    def double_up(start):
        while True:
            yield start
            start *= 2

    # merge sort without recursion
    def sortList(self, head):
        if not (head and head.next):
            return head

        dummy = ListNode(0)
        dummy.next = head

        for sub_len in double_up(1):
            processed = dummy
            remained = processed.next
            one_pass_no_remained = False
            merge_round = 0
            while remained:
                l1_and_l2 = []
                while len(l1_and_l2) < 2:
                    l1_and_l2.append(remained)
                    sub_count = 0
                    tail = None
                    while sub_count < sub_len and remained:
                        tail = remained
                        remained = remained.next
                        sub_count += 1
                    if tail:
                        tail.next = None

                l1, l2 = l1_and_l2
                if not l2:  # then, no remained too
                    processed.next = l1
                else:
                    while l1 or l2:
                        if (not l2) or (l1 and l1.val <= l2.val):
                            node = l1
                            l1 = l1.next
                        else:
                            node = l2
                            l2 = l2.next
                        processed.next = node
                        processed = processed.next

                merge_round += 1
                one_pass_no_remained = (merge_round == 1 and not remained)
            if one_pass_no_remained:
                break
        return dummy.next
"""
