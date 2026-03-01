# given two strings 

# s1 and s2 are isomorphic
#   -if they are completely different 
#     -yaani agar ek word hai manle truck 
#       -dusra word hai slump 
#       -agar tu har word ko identical mapping karega toh isomorphic hoga








class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        check = dict()# we use a dictionary that contaimnsboth values and ist keys
# we baically use thtidea that i ft the key exists it should alwys be the same value 
# and if the key doesnt exist add  anew key before cheking thtat the same value is not assigned to  a different key 

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
        #when the two conditions of unique mapping of keys and 
        #ensuring that the value does not belong to a prior key   
        #are confirmed then we can conclude that the string are isomorphioc   


