class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictt = { 2 : 'abc' , 3 : 'def', 4: 'ghi' , 5 : 'jkl' , 6: 'mno' , 7: 'pqrs' , 8: 'tuv' , 9: 'wxyz'}
        ans = []
        if len(digits) == 0:
            return ans
        def backtrack(st , start):
            if len(st) == len(digits):
                ans.append(st)
                return

            digit = digits[start]
            letters = dictt[int(digit)]

            for i in range(len(letters)):
                st += letters[i]
                backtrack(st , start + 1)
                st = st[:-1]

        backtrack('' , 0)
        return ans
            




        


        