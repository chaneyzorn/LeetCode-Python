from importlib import import_module


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


def create_linked_list(els):
    curr = dummy = ListNode(0)
    for val in els:
        node = ListNode(val)
        curr.next = node
        curr = curr.next
    return dummy.next


def get_solution(name):
    module = import_module(f"src.{name}")
    solution = getattr(module, "Solution")
    return solution()
