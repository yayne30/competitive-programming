class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixsum=[]
        tempsum=0
        for i in range(len(nums)):
            tempsum+=nums[i]
            prefixsum.append(tempsum)
        totalsum=prefixsum[len(nums)-1]
        middleindex=-1
        for j in range(len(prefixsum)):
            if(totalsum-prefixsum[j]==prefixsum[j]-nums[j]):
                return j
            
        return middleindex


        