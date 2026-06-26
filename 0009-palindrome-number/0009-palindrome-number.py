class Solution(object):
    def isPalindrome(self, x):
        z=x
        r=0
        while x>0:
            y=x%10
            x=(x-y)/10
            r=r*10+y
        return r==z
            
    
        """
        :type x: int
        :rtype: bool
        """
        