class Solution {
public:
    int removeDuplicates(vector<int>& nums) 
    {
        int l=nums.size();
        

        for (int i=0 ; i<l; i++)
        {
            int j = i+1;
            while (j<l)
            {
                if ( nums[i]==nums[j])
                {
                    nums.erase(nums.begin()+(j-1));
                    l--;
                }
                else
                {
                    j++;
                }
                
            }

        }
        return nums.size();
        
    }
};