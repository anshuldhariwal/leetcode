class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1

        counter = 1
        max_counter = counter

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                counter += 1
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 1

        if counter > max_counter:
            max_counter = counter

        return max_counter
