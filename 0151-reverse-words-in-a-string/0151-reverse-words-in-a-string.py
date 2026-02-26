# Given an input string s, reverse the order of the words.
# yani last word ko swap karde fisrt k ssaath

# The words in s will be separated by at least one space.
# jese hi space detect kara wese hi word khatam hua 


# Return a string of the words in reverse order concatenated by a single space.
# words ko ek spce k saath hi return karna hia



# multiple spaces between two words The returned string should only have a single space separating the words
# basically the first spac you encounter bas wahi tak tera word exist karega


# "the sky is blue"

# -string le  seedha chal 
#    - jese hi space aae rukja\
    #    space encounter par hone par left ko aage badha 
    #    agar left se aae toh a
    #    agar no space toh swap kar dononko phir left right aager badhd 


#      -2 pointer approach laga
       
       
# "blue is sky the"


class Solution:
    def reverseWords(self, s: str) -> str:

        cl = list(s)
        #left , right = 0 , len(s) -1 

        words = s.split()
        words.reverse()

        
        return " ".join(words)

        