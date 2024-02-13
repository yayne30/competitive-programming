class Solution:
    def maxScore(self, s: str) -> int:
        one=s.count('1')
        result=0
        zero=0
        for i in range(len(s)-1):
            if s[i]=='1':
                one-=1
            else:
                zero+=1
            result=max(result,zero+one)
        return result


        




        