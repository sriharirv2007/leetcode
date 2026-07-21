class Solution(object):
    def searchInsert(self, nums, target):
        for i,v in enumerate(nums):
            if v>=target:
                return i
            if nums[len(nums)-1]<target:
                return len(nums)
            
    
        

    