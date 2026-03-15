class Solution:
    def jump(self, nums: List[int]) -> int:

        jump = 0 

        curr_end = 0 

        farthest = 0

        for i in range(len(nums) -1 ): 
            farthest = max(farthest , nums[i] + i )  
            

            if curr_end == i :
                jump+=1
                curr_end  = farthest

              
        return jump

