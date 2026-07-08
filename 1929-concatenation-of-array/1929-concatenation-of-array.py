class Solution(object):
    def getConcatenation(self, nums):
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        