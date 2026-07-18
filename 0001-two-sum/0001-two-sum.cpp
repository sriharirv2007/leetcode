class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int l;
        l=nums.size();
        for (int i=0 ; i<l; i++)
        {
            for (int j=i+1 ; j<l; j++)
            {
                int s = nums[i]+nums[j];
                if (s==target)
                {
                

                  return {i,j};

                }
            
            }
        }
        return {};
        
    }
};