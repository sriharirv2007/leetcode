class Solution(object):
    def maxProduct(self, n):
        x=[0,0]
        while n:
            r=n%10
            x.append(r)
            x.remove(min(x))
            n/=10
        p=x[0]*x[1]
        return p

    
        """
        :type n: int
        :rtype: int
        """
        