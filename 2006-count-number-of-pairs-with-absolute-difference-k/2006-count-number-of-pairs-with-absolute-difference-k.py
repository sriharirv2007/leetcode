class Solution(object):
    def countKDifference(self, nums, k):
       





        count=0
        for m,i in enumerate(nums):
            for n,j in enumerate(nums):
                if abs(i-j)==k and m!=n:
                    count+=1
        return count/2



        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        