# 2 integers  and then give out combinations for given range 1 , n and size of subarray woudl be 

# 1 2 is the same as 2 1 toh no duplicates toh wo bhi skip karna 







class Solution:
    def helper(self, start:int , result :List[int], size: int ,limit:int, final : List[List[int]] ):
     
     if(size == len(result)):
        final.append(result.copy())
        return  

     for i in range(start , limit+1) :
        result.append(i)
        self.helper(i +1 , result , size ,limit ,final)  
        result.remove(i) 

  






    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        combi = []

        self.helper(1 , combi , k , n , ans)

        return ans

        
        