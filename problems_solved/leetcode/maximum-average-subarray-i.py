class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        accum=[0]*(len(nums)+1)
        accum[1]=nums[0]

        for i in range(2,len(nums)+1):
            accum[i]=accum[i-1]+nums[i-1]
        print(accum)
        
        l=1
        r=k
        avg_max=float(-inf)

        while r<=len(nums):
            avg=float((accum[r]-accum[l-1])/k)
            print(avg)
            avg_max=max(avg_max,avg)
            l+=1
            r+=1

        return avg_max




        