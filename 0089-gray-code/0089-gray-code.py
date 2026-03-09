class Solution:
    def grayCode(self, n: int) -> List[int]:
        

       
      


            ans  = [0,1]
           
            for i in range(1 , n)  :
                newlist = []
                
                for j in reversed(ans):
                    newlist.append(j + 2**(i))
                ans +=newlist    

            return ans

                 



        