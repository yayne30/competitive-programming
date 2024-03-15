class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l = 1
        h = x 
        while l < h:
            mid = l + ((1 + h - l ) // 2)
            if mid ** 2 > x:
                h = mid - 1
            elif mid ** 2 <= x:
                l = mid
        return l
            


        
        