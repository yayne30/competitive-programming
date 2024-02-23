class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        result=0
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                top=stack.pop()
                v=max(1,2*top)
                stack[-1]+=v
        return stack.pop()

