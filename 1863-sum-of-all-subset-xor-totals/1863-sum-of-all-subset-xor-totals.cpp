class Solution {
public:
 int total = 0 ;

    void solve(vector<int> &arr , int index , int currentxor ){
        if(index == arr.size()){
            total += currentxor ; 
            return;
        }

        solve(arr , index +1 , currentxor ^ arr[index]);
        //this upar wala is done to include the arr index

        solve(arr, index +1 , currentxor);
        //this is done to exclude the arrr index

    }

    int subsetXORSum(vector<int>& nums) {
        solve(nums, 0 , 0);
        return total ;

        
       
        
    }
};