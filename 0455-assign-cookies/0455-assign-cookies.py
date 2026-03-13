# solviong greedy problem requires us to think of the best solutuion at that step if we hav eth best opyimal solution at that step then we are ready to have the best local solution at every step and then having the best answer at th ene d

# ubnlike backtracking in greeedy we diont have to find or explore all possible solutions 

# thi ssusulally involvers sortuing first and then iteratinng 


# also involves chooisng the largest and smalles tbest option available



class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left  = 0 
        count = 0
        right = 0

        while left  < len(g) and right < len(s):
            if s[right] - g[left]  >= 0 :
                count+=1
                left+=1
                right+=1

            elif g[left]  > s[right] :
                
                right+=1

        return count

        