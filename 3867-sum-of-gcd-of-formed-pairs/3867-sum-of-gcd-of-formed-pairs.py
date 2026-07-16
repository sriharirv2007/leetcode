class Solution(object):
    def gcdSum(self, nums):
        if not nums:
            return 0
            
        p = []
        mx = 0 
        for i in nums:
            if i > mx:   
                mx = i
            y = mx       
            while i:
                y, i = i, y % i
            p.append(y)
        p.sort()
        
        s = 0
       
        left = 0
        right = len(p) - 1
        
        while left < right:
            m = p[right]
            n = p[left]
            
            right -= 1
            left += 1
            
            while n:
                m, n = n, m % n
            s += m
            
        return s
        



        """
        :type nums: List[int]
        :rtype: int
        """
        