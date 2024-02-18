import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local=0
        globalm=float('-inf')
        for i in nums:
            local=max(i,i+local)
            if local>globalm:
                globalm=local
        return globalm
        