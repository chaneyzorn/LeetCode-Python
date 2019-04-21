class Solution:
    def VerifySquenceOfBST(self, sequence):
        def recurse(sequence, start, end):
            if start >= end:
                return True
            i = end - 1
            while i >= start and sequence[i] > sequence[end]:
                i -= 1
            for j in range(start, i):
                if sequence[j] > sequence[end]:
                    return False
            return recurse(sequence, start, i) and recurse(sequence, i + 1, end - 1)

        if not sequence:
            return False
        return recurse(sequence, 0, len(sequence) - 1)
