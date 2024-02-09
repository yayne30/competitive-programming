class Solution(object):
    def runningSum(self, nums):
        sum=0
        result=[]
        for i in range (len(nums)):
            sum=sum+nums[i]
            result.append(sum)
        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """