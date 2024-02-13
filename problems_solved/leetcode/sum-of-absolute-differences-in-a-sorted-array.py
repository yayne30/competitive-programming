class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        accum=[0]*(len(nums)+1)
        temp=0
        for i in range (len(nums)):
            temp+=nums[i]
            accum[i+1]=temp
         

        for i in range(len(nums)):
            a=i*nums[i]-accum[i]
            if i<len(nums)-1:
                b=accum[len(accum)-1]-accum[i+1]-((len(nums)-1-i)*nums[i])
                
            else:
                b=0
            result[i]=a+b
        return result