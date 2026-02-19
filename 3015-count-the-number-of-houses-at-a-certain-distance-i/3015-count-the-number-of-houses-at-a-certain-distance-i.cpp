class Solution {
public:
    vector<int> countOfPairs(int n, int x, int y) {
        vector<int> ans(n,0);
        int dist  = 0 ;
       

        for(int i = 1  ;i <= n ; i++){
            for(int j = i+1 ; j <=n ; j++){
                
                int d1 = abs(i-j);
                int d2 = abs(i-x) +1 +abs(y-j);
                int d3 = abs(i-y)+ 1 + abs(j-x);

                dist = min(d1 ,(min(d2, d3)) );
               

                ans[dist-1]+=2 ;
            }

        }
        return ans;
        
    }
};