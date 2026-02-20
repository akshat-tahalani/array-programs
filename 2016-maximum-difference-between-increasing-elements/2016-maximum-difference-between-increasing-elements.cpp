class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int maxdiff = 0 ;

        for(int i = 0 ; i <nums.size()-1;  i++){
            for(int j = i+1 ; j < nums.size(); j++){
                if( i<j && nums[i] < nums[j] ){
                    maxdiff = max (maxdiff , nums[j] - nums[i]);
                }

            }
        }
        return maxdiff != 0 ? maxdiff : -1;
        
    }
};