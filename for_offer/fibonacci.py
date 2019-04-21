class Solution:
    def Fibonacci(self, n):
        curr, next = 0, 1
        while n:
            next += curr
            curr = next - curr
            n -= 1
        return curr

    # def Fibonacci(self, n):
    #     if n <= 1:
    #         return n
    #
    #     prev, result = 0, 1
    #     while n >= 2:
    #         temp = prev
    #         prev = result
    #         result += temp
    #         n -= 1
    #     return result
