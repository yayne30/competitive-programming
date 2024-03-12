class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        if nums[0] > 0 and len(nums) < 3:
            return result

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                if summ < 0:
                    start += 1
                elif summ > 0:
                    end -= 1
                else:
                    result.append([nums[start],nums[end],nums[i]])
                    s = nums[start]
                    e = nums[end]
                    while start < end and s == nums[start]:
                        start += 1
                    while start < end and e == nums[end]:
                        end -= 1

        return result








        
                



        