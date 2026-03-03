# given integer is happy ort not 

# start with number replace the number by sum of square of its digits 

# repreat the process untill number equals 1 

# if all 1 then happy 







class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen =set()
        sqsum = 0

       
        while(sqsum not in seen and sqsum != 1) :
            sqsum = 0
            
            
            seen.add(n)
            while n!=0 : 
                sqsum += (n%10) **2
                n= n//10
           
            
            n = sqsum  
            
        return sqsum == 1 
           

      


           

        
        


        
        

        
        