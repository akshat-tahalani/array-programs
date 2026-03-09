class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        gsum = 0

        

        def helper(i , j) :


            
            if i < 0 or j < 0 or j>= len(grid[0]) or i >= len(grid):
                return 0
            
            if grid[i][j] == 0 :
                return 0

            

            val = grid[i][j]

            grid[i][j]= 0
             
            result = max(helper(i+1, j), helper(i , j+1) , helper( i-1 , j) , helper(i , j-1)) 
            
            grid[i][j] = val 
            
            
            return val + result

        


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
              gsum = max (gsum , helper (i,j)) 

        return gsum
                