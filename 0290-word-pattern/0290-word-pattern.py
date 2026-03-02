class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        check = dict()

        if len(words) !=len(pattern) :
            return False

        for i in range(len(pattern)):
            if pattern[i] not in check:
                if words[i] in check.values():
                    return False
                else:
                    check[pattern[i]] = words[i]   

            else:
                if check[pattern[i]] != words[i]:
                    return False

        return True        
                         

            
            
        