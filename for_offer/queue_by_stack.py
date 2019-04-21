class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    # def push(self, node):
    #     while self.stack_2:
    #         self.stack_1.append(self.stack_2.pop())
    #     self.stack_1.append(node)
    #     while self.stack_1:
    #         self.stack_2.append(self.stack_1.pop())
    #
    # def pop(self):
    #     if not self.stack_2:
    #         return None
    #     return self.stack_2.pop()
