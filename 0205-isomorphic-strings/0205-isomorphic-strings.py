# given two strings 

# s1 and s2 are isomorphic
#   -if they are completely different 
#     -yaani agar ek word hai manle truck 
#       -dusra word hai slump 
#       -agar tu har word ko identical mapping karega toh isomorphic hoga








class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        check = dict()


        for i in range(len(s)):
            if s[i] not in check:
                if t[i] in check.values():
                    return False
                else:
                    check[s[i]]= t[i]

                
            else:
                if check[s[i]] != t[i] :
                    return False
              

        return True            


