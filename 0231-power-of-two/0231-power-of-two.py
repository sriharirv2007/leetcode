class Solution(object):
    def isPowerOfTwo(self, n):
        i=0
        while True:
            if 2**i==n:
                return True
            elif 2**i>n:
                return False
            i+=1
        """
        :type n: int
        :rtype: bool
        """
        