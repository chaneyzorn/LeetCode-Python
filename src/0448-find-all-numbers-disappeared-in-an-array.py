class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]

    # def findDisappearedNumbers(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     for i, num in enumerate(nums):
    #         if num != i + 1:
    #             next = nums[num-1]
    #             nums[num-1] = num
    #             while next != nums[next-1]:
    #                 temp = nums[next-1]
    #                 nums[next-1] = next
    #                 next = temp
    #
    #     result = []
    #     for i, num in enumerate(nums):
    #         if num != i + 1:
    #             result.append(i + 1)
    #     return result


if __name__ == '__main__':
    result = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(result)
