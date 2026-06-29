class Solution(object):
    def plusOne(self, digits):
        n=0
        l=[]
        for i in range(0,len(digits)):
            n=n*10+digits[i]
        n+=1
        while n:
            r=n%10
            n//=10
            l.append(r)
        l.reverse()
        return l
           
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        