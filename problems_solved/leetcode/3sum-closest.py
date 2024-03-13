class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiff = float(inf)
        ans = 0
        if len(nums) == 3:
            return sum(nums)
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                diff = abs(target - summ)
                if summ == target:
                    return summ
                else:
                    if diff < mindiff:
                        mindiff = diff
                        ans = summ
                if summ < target:
                    start += 1
                elif summ > target:
                    end -= 1
        return ans


            
            
            
        return summ

            
            
        