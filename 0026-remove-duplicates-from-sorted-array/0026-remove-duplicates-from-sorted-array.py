class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    nums.pop(j)
                else:
                    j+=1
        l=len(nums)
        return l
        """
        :type nums: List[int]
        :rtype: int
        """
        