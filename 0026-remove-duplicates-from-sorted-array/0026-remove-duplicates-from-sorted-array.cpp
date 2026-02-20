class Solution {
public:
    int removeDuplicates(vector<int>& v) {
        int n =  v.size();
        if (n==0 ){
            return 0; 
        }
        
        
        int k = 1 ;

        for(int i  =1; i < n ; i++){
            if(v[i]!=v[i-1]){
                v[k]= v[i];
                k++;
            }
        }
        return k ;  

      
    }
};