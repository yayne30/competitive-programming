class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixFreq={0:1}
        prefixsum=0
        count=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            targetsum=prefixsum-k
            if targetsum in prefixFreq:
                count+=prefixFreq[targetsum]
            prefixFreq[prefixsum]=1+prefixFreq.get(prefixsum,0)
        return count



        
        



        
        