class Solution:
    def simplifyPath(self, path: str) -> str:
        p=list(path.split('/'))
        ans=''
        stack=[]
        for i in p:
            if i!='' and i!='..' and i!='.':
                stack.append(i)
            elif i=='..' and stack:
                stack.pop()
        for i in stack:
            ans+='/'
            ans+=i
        if ans=='':
            return '/'
        return ans
            
            
            


