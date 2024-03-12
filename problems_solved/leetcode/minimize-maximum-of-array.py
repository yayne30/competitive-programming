class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        ans = nums[0]
        summ = nums[0]

        for i in range (1,len(nums)):
            summ += nums[i]
            curr = ceil(summ / (i + 1))
            ans = max(ans, curr)
        
        return int(ans)






        # first approach but didn't work for some test cases
        # leng = len(nums)
        # for i in range(leng - 1, -1, -1):
        #     if i > 0:
        #         if nums[i] > nums[i - 1]:
        #             x = nums[i]
        #             y = nums[i - 1]
        #             diff = x - y
        #             nums[i - 1] += ceil(diff / 2)
        #             nums[i] -= ceil(diff / 2)
             

        # return max(nums)
