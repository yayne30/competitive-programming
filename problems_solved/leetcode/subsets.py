class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(arr , start):
            ans.append(arr[:])
            for i in range(start , len(nums)):
                arr.append(nums[i])
                backtrack(arr[:] , i + 1)
                arr.pop()

        backtrack([], 0)
        return ans

        