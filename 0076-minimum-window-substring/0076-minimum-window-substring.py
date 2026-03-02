class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen =0  
        left  = 0 
        winsize = float('inf')
        fleft = 0 
        fright = 0 
        
        counter = len(t)

        check = dict()

        for x in t :
            if x not in check:
                check[x] =1
            else:
                check[x] +=1


        for right in range(len(s)):
            if s[right] in check:
                check[s[right]] -=1
                if check[s[right]] >= 0:
                    counter -=1

                
            
            
            while counter ==0 :
                currwinsize = right -left + 1

                if(currwinsize < winsize):
                    winsize = currwinsize
                    fleft =left 
                    fright =right

                    
                if s[left] in check:
                    check[s[left] ]+=1
                    if check[s[left]] >  0:
                        counter+=1
                left+=1        

                     
        

        return "" if winsize == float('inf') else s[fleft : fright +1] 
        
