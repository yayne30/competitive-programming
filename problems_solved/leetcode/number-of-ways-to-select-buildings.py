class Solution:
    def numberOfWays(self, s: str) -> int:
        totalone=s.count('1')
        totalzero=s.count('0')
        currone=0
        currzero=0
        result=0
        for i in s:
            if i=='0':
                result+=(currone*(totalone-currone))
                currzero+=1
            elif i=='1':
                result+=(currzero*(totalzero-currzero))
                currone+=1
        return result








                


        