class Solution(object):
    def twoSum(self, nums, target):
        for m,i in enumerate(nums):
            for n,j in enumerate(nums):
                if i+j==target and n!=m:
                    return [m,n]
                    

       
            

           

            
        
            
        
            

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        