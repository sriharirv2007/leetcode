class Solution(object):
    def sortColors(self, nums):
        a = b = c = 0

        for x in nums:
            if x == 0:
                a += 1
            elif x == 1:
                b += 1
            else:
                c += 1

        nums[:] = [0] * a + [1] * b + [2] * c
                


        