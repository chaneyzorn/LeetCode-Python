class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        mid, l, r = 0, 0, len(rotateArray) - 1

        while rotateArray[l] >= rotateArray[r]:
            if r - l == 1:
                mid = r
                break
            mid = l + (r - l) // 2
            if rotateArray[l] == rotateArray[mid] == rotateArray[r]:
                return self.scan(rotateArray)
            if rotateArray[mid] >= rotateArray[l]:
                l = mid
            else:
                r = mid
        return rotateArray[mid]

    def scan(self, rotateArray):
        if not rotateArray:
            return 0
        prev = rotateArray[0]
        for curr in rotateArray[1:]:
            if curr < prev:
                return curr
        return prev
