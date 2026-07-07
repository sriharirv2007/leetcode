class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        s=0
        y=x
        while x:
            r=x%10
            x//=10
            s=s+r
        if (y%s==0) :
            return s
        return -1
        
       
       
        """
        :type x: int
        :rtype: int
        """
        