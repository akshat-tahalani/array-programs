# se a dictionary to store the frequency of each character in t. Use a counter starting at len(t) to track how many characters still needed.
# Expand right through s. When s[right] is in the dict, decrement its frequency. Only decrement counter if the frequency is still >= 0 after decrementing — this ensures we only count genuinely needed characters, not extras.
# When counter hits 0, we have a valid window. Record it if it's the smallest so far using fleft and fright.
# Then shrink from the left. When removing s[left], if it's in the dict, increment its frequency back. If the frequency goes above 0, we lost a needed character so increment counter back up. Then move left forward.
# Keep shrinking in a while loop as long as counter is 0. Once counter goes back up, expand right again.
# At the end return s[fleft:fright+1], or "" if no valid window was ever found.


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
        
