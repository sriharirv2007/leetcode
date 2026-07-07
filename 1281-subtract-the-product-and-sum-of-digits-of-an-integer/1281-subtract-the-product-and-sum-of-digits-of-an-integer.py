class Solution(object):
    def subtractProductAndSum(self, n):
        s=0
        p=1
        while n:
            r=n%10
            n//=10
            s+=r
            p*=r
        return p-s
        """
        :type n: int
        :rtype: int
        """
        