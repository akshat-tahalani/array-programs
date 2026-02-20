class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int initial=0;//basically apan no zeros ko left me shift kar rahe
        for(int i = 0 ; i<nums.size(); i++){
            if(nums[i]!=0){
                swap(nums[i],nums[initial]);
                initial++;
            }
           
        }
        
    }
};