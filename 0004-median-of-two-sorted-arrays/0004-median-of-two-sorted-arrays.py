class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        fl=nums1+nums2
        fl.sort()
        if len(fl)%2==0:
            x=len(fl)/2
            return (fl[x-1]+fl[x])*(0.5)
        else:
            x=(len(fl)+1)/2
            return fl[x-1]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        