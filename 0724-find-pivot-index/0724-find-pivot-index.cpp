class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int totalsum = 0 ;
        
        int lsum = 0 ; 
        

        for(int i = 0 ;i<=n-1 ; i++){
            totalsum += nums[i];  
        }


        for(int i = 0 ;i < n ;i++){
            int rightsum = totalsum -lsum -nums[i];
            if(lsum == rightsum){
                return i;
            }
            lsum += nums[i];


        }
        
     
        return -1;



    
    }
};