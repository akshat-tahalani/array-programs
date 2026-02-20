class Solution {
public:

    void helper(vector<int> arr ,int index  ,int remtarg, vector<int>  &currcombi , vector<vector<int>> &result){
        

        if(remtarg == 0 ){
            result.push_back(currcombi);
            return;

        }

        if(index == arr.size()){
            return ;

        }

        if(remtarg<0 ){
            return;

        }

        //there will be to option to either keep repeating the same 

        //element to be added into the target sum
        // 2nd choice would be to move to the nect element

        currcombi.push_back(arr[index]);


        helper( arr ,index , remtarg-arr[index], currcombi ,result ) ;


        currcombi.pop_back();
       
        helper(arr , index +1 , remtarg, currcombi , result);

    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> ans;
        vector<vector<int>>  yo ;

        helper(candidates , 0 , target , ans , yo);

        return yo ;
        
    }
};