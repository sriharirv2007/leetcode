class Solution(object):
    def maximum69Number (self, num):
        n=int(str(num)[::-1])
        s=n
        count=0
        val=0
        while s:
            r=s%10
            s//=10
            if r==6:
                val=+1
                break
            count+=1
        if val:
            n=n+3*10**count
        z=int(str(n)[::-1])
        return z


        
        
     


       

        
        """
        :type num: int 
        :rtype: int
        """
        