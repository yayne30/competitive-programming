class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad,dire=deque(),deque()
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=="R":
                rad.append(i)
            else:
                dire.append(i)
        while rad and dire:
            if rad[0]<dire[0]:
                rad.append(n)
            else:
                dire.append(n)
            rad.popleft()
            dire.popleft()
            n+=1
        return 'Radiant' if rad else "Dire"


        # stack=[senate[0]]
        # for i in range(1,len(senate)):
        #     if stack and stack[-1]!=senate[i]:
        #         stack.pop()
        #     else:
        #         stack.append(senate[i])
        # if stack.pop()=='R':
        #     return "Radiant"
        # else:
        #      return "Dire"
            
        