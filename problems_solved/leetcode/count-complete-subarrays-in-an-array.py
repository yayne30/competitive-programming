class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        sett=set()
        count=0
        for i in nums:
            sett.add(i)
        k=len(sett)
        left=0
        for i in range(len(nums)):
            subset=set()
            for j in range(i,len(nums)):
                subset.add(nums[j])
                if len(subset)==k:
                    count+=1
        return count

        