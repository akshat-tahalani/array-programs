class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left = 0 
        right = 0
        maxreach = 0 
        
       

        for i in range(len(nums)):

            if i > maxreach:
                return False
           
            maxreach = max( maxreach  ,i+ nums[i])



           
        return True
                
        