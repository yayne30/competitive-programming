class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]













        # ans = float('inf')

        # def recur(nums):
        #     nonlocal ans
        #     l = 0
        #     r = len(nums) - 1
        #     if l == r:
        #         return nums[l]
        #     mid = l + (r - l) // 2
        #     if nums[mid] > nums[r]:
        #         ans = min(ans, recur(nums[mid + 1: r + 1]))  
        #     elif nums[mid] < nums[r]:
        #         ans = min(ans, recur(nums[l: mid + 1]))
        #     return ans
        
        # return recur(nums)