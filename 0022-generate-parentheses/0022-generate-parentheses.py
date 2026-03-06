# n is an integer

# malum hai ki recursion use hoga kyoki simply bas apana repeat karte jaa rahe haiowrds ko 


# har baar valid parenthesis hi print ho rahe hai 







class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []        
        



    


        def helper(ans , final ,opencount , closecount  ):
            
            if opencount==closecount and closecount ==n :
                final.append("".join(ans))
                return

            if opencount < n:
                ans.append('(')
                helper(ans , final ,opencount+1 , closecount  )
                ans.pop()


            if closecount < opencount:
                ans.append(')')   
                helper(ans , final ,opencount , closecount+1  ) 
                ans.pop()
                
        

        helper( [], final,0 , 0)
        return final




             


        
        