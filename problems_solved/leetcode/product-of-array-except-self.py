class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        [1,2,3,4]
        """
        result=[1]*len(nums)
        leftproduct=1
        for i in range(len(nums)):
            result[i]=leftproduct
            leftproduct*=nums[i]
        rightproduct=1
        for j in range(len(nums)-1,-1,-1):
            result[j]*=rightproduct
            rightproduct*=nums[j]
        return result







        

        
       



        