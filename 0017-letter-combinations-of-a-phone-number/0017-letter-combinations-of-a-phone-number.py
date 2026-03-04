# string given from 2 to  9 




class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combi = []
        alpha = []

        if len(digits) == 0 : return []

        phone = { "2" : "abc" , "3" : "def" , "4" : "ghi" , "5" : "jkl" , "6" : "mno" , "7" : "pqrs" , "8" : "tuv" , "9" : "wxyz"  }

        def helper(combi,alpha):
            if len(combi) == len(digits) :
                alpha.append("".join(combi))
                return 

            for i in phone[digits[len(combi)]]:
                combi.append(i)
                helper(combi , alpha)
                combi.pop()
                

        helper([] , alpha) 
        return alpha       

                
        