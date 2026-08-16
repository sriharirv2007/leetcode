class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ar = []

        for x, i in enumerate(nums1):
            for y, j in enumerate(nums2):
                if i == j:
                    for k in range(y + 1, len(nums2)):
                        if nums2[k] > j:
                            ar.append(nums2[k])
                            break
                    else:
                        ar.append(-1)
                    break

        return ar
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        