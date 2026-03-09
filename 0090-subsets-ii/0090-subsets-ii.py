class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()


        def helper(index , ans  , combi):
            seen  = set()

           

            ans.append(combi.copy())    

            for i in range(index  ,len(nums)) :

                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                combi.append(nums[i])

                

                helper(i+1 , ans , combi)

                combi.pop()
                
                #helper(index +1  ,ans , combi)

        helper(0 , ans , [])
        return ans
        