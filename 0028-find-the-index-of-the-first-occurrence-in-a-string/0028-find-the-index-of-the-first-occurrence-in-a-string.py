# 2 string di hai needle aurhaystack 


# index dena hai initial when the needle exists in the haystack

# check karna that the needle is the part of the haystack
#  -limiter apna needle rahega
#    -yaani agar index i <  size of needle
#      - tabtak if needle [ i ]  =haystack [ i] ++ dono ko 
#       - ???

# apan ese bhi kar sakt eki while dono k char equal ho lekin usnm agar start of th word nahi hoga toh kaam nahi karega

# for loop 
#   -compare will do the first case

#   while()
#   agar equal do nothing
#    agar not equal exit loop return -1 edge case phel handle hoga 














class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)

        if l2>l1 : return -1

        for i in range(l1 - l2 +1) :
            if haystack[i : i+ l2] == needle :
              return i 

        return  -1    

