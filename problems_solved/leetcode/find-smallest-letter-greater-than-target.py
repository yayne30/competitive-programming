class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(set(letters))

        if letters[-1] <= target or letters[0] > target:
            return letters[0]
        l = 0
        h = len(letters) - 1
        while l <= h:
            mid = l + ((h - l) // 2)
           # print(mid)
            if letters[mid] > target:
                h = mid - 1
            elif letters[mid] <= target:
                l = mid + 1
        return letters[l]
   
        
            



        


        