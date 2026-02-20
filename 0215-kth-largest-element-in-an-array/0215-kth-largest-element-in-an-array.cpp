class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue <int  , vector<int> , greater<int>> q1 ;

        for(int n : nums){
            q1.push(n);

            if(q1.size() > k ){
                q1.pop();

            }
        }
        return q1.top();

        
        
    }
};