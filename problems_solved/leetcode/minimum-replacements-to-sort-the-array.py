class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        mini=10**9 +1
        count=0
        for i in nums[::-1]:
            d=ceil(i/mini)
            count+=d-1
            mini=i//d
        # for i in range(n-1,-1,-1):
        #     if mini!=0:
        #         count+=ceil(nums[i]/mini)-1
        #         mini=nums[i]//ceil(nums[i]/mini)
        return count


        