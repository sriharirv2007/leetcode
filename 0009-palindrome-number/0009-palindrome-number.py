class Solution(object):
    def isPalindrome(self, x):
        z=x
        r=0
        while x>0:
            y=x%10
            x=(x-y)/10
            r=r*10+y
        if r==z:
            a=True
        else:
            a=False
        return a
            
    
        """
        :type x: int
        :rtype: bool
        """
        