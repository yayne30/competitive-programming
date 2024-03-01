class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        ans = 0
        for i in nums:
            if i != val:
                nums[ind] = i
                ind += 1
                ans += 1
        return ans
