class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftingarray=[0]*(len(s)+1)
        for i in range(len(shifts)):
            if shifts[i][2]==0:
                shiftingarray[shifts[i][0]]-=1
                shiftingarray[shifts[i][1]+1]+=1
            elif shifts[i][2]==1:
                shiftingarray[shifts[i][0]]+=1
                shiftingarray[shifts[i][1]+1]-=1
        
        for j in range(1,len(shiftingarray)-1):
            shiftingarray[j]+=shiftingarray[j-1]
           



        result=''
        for k in range(len(s)):
            result+=chr(((ord(s[k])+shiftingarray[k]-97)%26)+97)
        return result
        

        

        

        
        