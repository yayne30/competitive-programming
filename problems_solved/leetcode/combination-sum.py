class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(arr , start , target):
            if target == 0:
                ans.append(arr)
                return
            if target < 0:
                return 
            for i in range(start, len(candidates)):
                backtrack(arr + [candidates[i]], i , target - candidates[i] )
            
        backtrack([] , 0 , target)
        return ans





        