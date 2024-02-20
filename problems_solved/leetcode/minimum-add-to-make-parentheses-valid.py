class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')' and len(stack)==0:
                ans+=1
            elif i==')':
                stack.pop()
        return ans+len(stack)








        #         left+=2
        # if len(stack)==0:
        #     ad=len(s)-left
        # else:
        #     ad=0
        # return len(stack)+ad
        