class Solution(object):
    def searchInsert(self, nums, target):
        for i,v in enumerate(nums):
            if v>=target:
                return i
            if nums[len(nums)-1]<target:
                return len(nums)
            
    
        

    '''def lth(self,l,n,t):
        if n[l-1]<=t:
                if n[l-1]<t:
                    return l
                return l-1
        else:
            l=l//2
            if l==0:
                return 0
            return self.lth(l,n,t)

    def searchInsert(self, nums, target):
        l=len(nums)
        return self.lth(l,nums,target)'''
        

            
           


    
        