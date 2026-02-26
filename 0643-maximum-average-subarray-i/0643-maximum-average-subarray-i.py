# array nums given hai

# aur ek integer k 


# subarray nikalna hai length k ke baragbar 

# kykoi suybarray mention hua hai t oh slidng window wala concept use hoga









class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = float('-inf')

        for i in range(len(nums) - k +1) :
            curr_sum = 0 
            for j in range(k):
               curr_sum += nums[i+j]

            maxsum = max(maxsum , curr_sum)

        return maxsum/k         

            
        