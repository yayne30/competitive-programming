class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        zeroes = 0
        maxx = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zeroes += 1
            while zeroes > 1:

                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxx = max( maxx , i-left)
        
        return maxx




          


      
