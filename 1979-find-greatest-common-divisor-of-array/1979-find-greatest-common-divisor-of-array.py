class Solution(object):
    def findGCD(self, nums):
        x=min(nums)
        y=max(nums)
        while y:
            x,y=y,x%y
        return x
        """
        :type nums: List[int]
        :rtype: int
        """
        