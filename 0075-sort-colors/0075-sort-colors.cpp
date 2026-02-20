class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int h = nums.size()-1  , l = 0  , mid = 0 ; 
    while(mid<=h){


        if(nums[mid]==0){
            swap(nums[l], nums[mid]);
            mid++;
            l++;

        }
        else if(nums[mid]==1){
            mid++;

        }
        else{
            swap(nums[mid],nums[h]);
            h--;


        }
    }
    
        
    }
};