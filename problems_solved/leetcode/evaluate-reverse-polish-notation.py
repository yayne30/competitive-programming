class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        result=0
        for i in tokens:
            if i=='+':
                result=stack.pop()+stack.pop()
                stack.append(result)
            elif i=='-':
                a,b=stack.pop(), stack.pop()
                stack.append(b-a)
            elif i=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            elif i=='*':
                result=stack.pop()*stack.pop()
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()

            


            
        