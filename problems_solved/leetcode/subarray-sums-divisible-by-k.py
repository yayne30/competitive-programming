class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modfreq={0:1}
        temp=0
        mod=0
        count=0
        for i in range(len(nums)):
            temp+=nums[i]
            mod=temp%k
            if mod in modfreq:
                count+=modfreq[mod]
            modfreq[mod] = modfreq.get(mod, 0) + 1
        return count
            

            

            
        




        