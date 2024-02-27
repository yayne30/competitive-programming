class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                curr=''
                while stack and stack[-1]!='[':
                    curr=stack.pop()+curr
                stack.pop()
                k=''
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*curr)
        return ''.join(stack)



            





        