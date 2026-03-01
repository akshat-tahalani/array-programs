# two strings a and b 

# return true if you can return a from using letters in b 

# no duplicates 


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #isthere = False
        seen  = dict()

        for c in magazine :
            if c not in seen:
                seen [c] =1 
            else:
                seen[c]+=1 
            

        for x in ransomNote:
           if x not in seen or seen[x] == 0:
            return False
           
           else:
            seen[x] -=1 
            
                
           
        
        return True        