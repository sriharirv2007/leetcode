class Solution(object):
    def reverse(self, x):
        r=0
        s=-1 if x<0 else 1
        x=abs(x)
        while x:
            z=x%10
            x//=10
            r=r*10+z
        if -2**31 <= r <= 2**31 - 1:
            return s*r
        else:
            return 0
            
       
                     
            
           
        
        
            



        """
        :type x: int
        :rtype: int
        """
        