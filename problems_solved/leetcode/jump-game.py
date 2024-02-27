class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        l=len(nums)-2
        r=len(nums)-1
        flag=False
        while l>=0:
            if nums[l]>=r-l:
                flag=True
                l-=1
                r=l+1
                
            elif nums[l]<r-l and l==0:
                flag=False
                l-=1
            else:
                l-=1
        return flag
