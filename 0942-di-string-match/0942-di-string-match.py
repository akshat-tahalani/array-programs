class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s) + 1
        left = 0 
        right =  n-1
        
        result = []

       
        for i in range(len(s)):
            if s[i] == 'I':
                result.append(left)
                left+=1
                
            else:
                result.append(right)
                
                right-=1
        
        if left == right:
            result.append(right)

        return result


        
            