# given integer is happy ort not 

# start with number replace the number by sum of square of its digits 

# repreat the process untill number equals 1 

# # Take a number. Break it into its individual digits, square each digit, and add them all up to get a new number. Repeat this process with the new number.
# If you eventually reach 1, it's a happy number. If you never reach 1 and instead keep looping forever through the same numbers, it's not happy.
# So your job is to detect those two cases — either you hit 1, or you see a number you've already seen before which means you're in a cycle.







class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen =set()
        sqsum = 0

       
        while(sqsum not in seen and sqsum != 1) :
            sqsum = 0
            
            
            seen.add(n) # and then when the loop resets adding the new n to the set 
            while n!=0 : 
                sqsum += (n%10) **2
                n= n//10
           
            
            n = sqsum  #basically restting the sqsum and making it  an ew one to 
            #be squared and added
            
        return sqsum == 1 
           

      


           

        
        


        
        

        
        