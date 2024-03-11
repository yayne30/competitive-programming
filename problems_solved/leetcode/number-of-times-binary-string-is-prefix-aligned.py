class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        maxx = -float(inf)
        ans = 0
        for i in flips:
            count += 1
            maxx = max(maxx , i)
            if maxx == count:
                ans += 1
            
        return ans
            



        