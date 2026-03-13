class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        left  = 0 

        while left < len(flowerbed) and n != 0  :

            if flowerbed[left] == 0 and ( left == len(flowerbed) -1 or flowerbed[left+1] != 1) and (left==0 or flowerbed[left-1] != 1):
                flowerbed[left] = 1
                n-=1 
                left+=1
                

            elif flowerbed[left] == 1 or flowerbed[left] == 0 :
                left+=1

        return n==0
        