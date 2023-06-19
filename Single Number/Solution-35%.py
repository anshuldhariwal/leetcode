class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 35%
        # stack = []

        # for i in nums:
        #     if i not in stack:
        #         stack.append(i)
        #     else:
        #         stack.pop(stack.index(i))

        # return stack[0]

        n = len(nums)
        c = 0
        for i in range(n):
            c = c ^ nums[i]
        return c
