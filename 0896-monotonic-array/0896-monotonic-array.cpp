class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
       
       bool isinc =true; 
       bool isdec = true ;

       for(int i = 1 ; i < nums.size() ; i++){
        if(nums[i] < nums[i-1]){
            isinc =false;
        }
        if(nums[i]>nums[i-1]){
            isdec = false;
        }
        
       }

       return isinc || isdec ;

        
    }
};