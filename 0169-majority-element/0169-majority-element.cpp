class Solution {
public:
    int majorityElement(vector<int>& nums) {

        int n  = nums.size(); 
        unordered_map <int , int> mp ;

        for(int n : nums){
            mp[n] ++ ;
        }

        for(auto it : mp){
            int element  = it.first;
            int frq = it.second;

            if(frq>n/2){
                return element;
            }
        }
        return 0;
      
    }
};