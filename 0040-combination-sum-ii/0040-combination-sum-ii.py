class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        ans = []

        def helper(ans, combi ,remsum ,index):

            if remsum == 0 : 
                ans.append(combi.copy())
                return

            if index == len(candidates)  :
                return

            if remsum < 0:
                
                return 

            

            for i in range(index,len(candidates)):

                if i>index and candidates[i] == candidates[i-1]:
                    continue
                
                combi.append(candidates[i])

                helper(ans, combi ,remsum - candidates[i] , i+1)

                combi.pop()

                

            

        helper(ans , [] , target , 0)
        return ans