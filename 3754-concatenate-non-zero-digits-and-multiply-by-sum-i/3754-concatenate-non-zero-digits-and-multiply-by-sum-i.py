class Solution(object):
    def sumAndMultiply(self, n):
        x=0
        s=0
        c=0
        while n:
            r=n%10
            n//=10
            s+=r
            if r!=0:
                x=r*(10**c)+x
                c+=1  
        return x*s



        """
        :type n: int
        :rtype: int
        """
        