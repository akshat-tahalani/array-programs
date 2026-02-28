# nums array and int k 

# 2 diff index value same lekin abs diff k  se kam hai

#  -slidng window condition hai ki elemenst should be 2 index away 
#    -yani fixed window hai 
#      -iska mtalab left aur right define kar aur dono ki aaage karte jaa


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left  = 0
        seen = set() 
        isthere = False 

        for i in range(len(nums)):
            if nums[i] in seen : 
                isthere =True
                break
            seen.add(nums[i])
            while len(seen) > k :
                seen.remove(nums[i-k])

        return isthere


         
                    



        