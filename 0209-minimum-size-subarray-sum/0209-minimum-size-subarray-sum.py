# array of poiostive integers


# given target 



# rteurn length of subarray


# the subarray array sum >= target
#    -kyoki subarrray ka sume nikalna hia 
#     -yaani sliding window use hogi
#      -ab isme apan variable sliding window use karenge
#       -jisme vlaid condition hai ki sum subarray ka >= taregt sum
#        -jese hi mila ek apan min_len ka variable bana denge 
#         -return min len








class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        left  = 0 
        currsum = 0 

        for right in range(len(nums)) :

            currsum += nums[right]
            while currsum >= target :
                currlen = right - left + 1
                minlen = min(minlen ,currlen)
                currsum -= nums[left]
                left+=1
                
            

            

        return minlen if minlen < float('inf') else 0
           
                     
                