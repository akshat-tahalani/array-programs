class Solution {
public:
    void getsubset(vector<int> & arr, vector<int> & ans , int i , vector<vector<int>> &storess){
        //int i ;
        if ( i==arr.size()){
            storess.push_back({ans});
            return ; 

        }

        //include
        ans.push_back(arr[i]);
        getsubset(arr ,ans , i+1 , storess);

        ans.pop_back();

        //exclude 
        getsubset(arr ,ans , i+1 , storess);

    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> storess;
        vector<int> ans ; 
        
        getsubset(nums , ans , 0 , storess);
        return storess;

        
    }
};