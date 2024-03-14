class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(arr , start):
            if sum(arr) == target:
                ans.append(arr[:])
                return
            if sum(arr) > target:
                return
            if start == len(candidates):
                return 
            for i in range(start , len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(arr , i + 1)
                arr.pop()
        backtrack ( [] , 0)
        return ans

          
                    





        