class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,1);

        for(int i = 1 ; i <n ; i ++){
            ans[i] = ans[i-1]*nums[i-1];//prefix yaani wo element chodke uske pehle ke element 
        }

        int suffix = 1 ;

        for(int i = n-2 ; i>=0 ; i--){//suffix yaani us element k baad k element 
            suffix = suffix * nums[i+1];
            ans[i] = suffix*ans[i];
        }
        return ans;//prefix * suffix return ho raha 
        //yaani wo element ko chodke uske pehle ke element aur uske baad k 
        //element apas me multiply hoke return ho rahe hai
    }
};