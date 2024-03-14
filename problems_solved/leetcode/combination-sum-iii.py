class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(arr ,start):
            if len(arr) == k and sum(arr) == n:
                ans.append(arr[:])
                return 
            if len(arr) > k:
                return 
            for i in range(start , 10):
                arr.append(i)
                print(arr)
                backtrack(arr , i + 1)
                arr.pop()
        backtrack([] , 1)
        return ans
        