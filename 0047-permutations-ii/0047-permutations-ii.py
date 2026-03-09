class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited= [False]* len(nums)
        ans = []
        nums.sort()

        def helper(visited , ans ,index):
            seen  = set()

            

            if index == len(nums):
                ans.append(nums.copy())

            for i in range(index , len(nums)):
                if nums[i] in seen :
                    continue
                seen.add(nums[i])    

                
                nums[i] , nums[index] = nums[index] ,nums[i]  
                helper(visited , ans  ,index +1)
                nums[i] , nums[index] = nums[index] ,nums[i]  

           
        helper(visited , ans , 0)
        return ans


        