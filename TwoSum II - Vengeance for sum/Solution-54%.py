class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1
        output = []

        while i < j:
            if numbers[i] + numbers[j] == target:
                output = [i+1,j+1]
                break
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return output

                
