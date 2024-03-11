class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        def per (start):
            if start == len(nums):
                result.append(nums[:])
            for i in range(start,len(nums)):
                nums[start],nums[i] = nums[i], nums[start]
                per(start+1)
                nums[start],nums[i] = nums[i], nums[start]
                
        per(0)
        return result
            

        