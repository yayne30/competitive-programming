class Solution:
    def minimumSteps(self, s: str) -> int:
        counter=0
        zero=0
        for i in  range(len(s)-1,-1,-1):
            if s[i]=='0':
                zero+=1
            elif s[i]=='1':
                print(counter)
                counter+=zero

        return counter

            

        