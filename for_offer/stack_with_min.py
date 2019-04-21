class Solution:
    def __init__(self):
        self.min_val = float("inf")
        self.stack = []

    def push(self, node):
        if node < self.min_val:
            self.stack.append(self.min_val)
            self.min_val = node
        self.stack.append(node)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_val:
            self.min_val = self.stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_val
