class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum=0
        count=0
        pref={0:1}
        for i in nums:
            running_sum+=i
            count+=pref.get(running_sum-goal,0)
            pref[running_sum]=pref.get(running_sum,0)+1
        return count






