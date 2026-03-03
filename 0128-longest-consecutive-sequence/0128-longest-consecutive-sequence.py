# ek array given hai

# uske elemenrts me se sabse badha seq dhundhna hai 

# hasmap me store karle 

# kyoki array k andar seq me sorted nahi hume ye batana hai ki in elemnets me se sabse badha seq konsa banega 

# isme  ye concept hai ki agara humarar number jo hum daal rahe seen k nadr





class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
       

        seen  = set()

        for i in nums:
            seen.add(i)

        for y in seen:
            if y-1 in seen:

                continue
            else:
                length = 0
                while y in seen:
                    y+=1
                    length+=1
                maxlen = max(maxlen , length)
        return maxlen        

        