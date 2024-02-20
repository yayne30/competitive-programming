class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch={}
        ans=0
        k=1
        odd=0
        for i in s:
            ch[i]=ch.get(i,0)+1
        if len(ch)==1:
            return len(s)
        for j in ch.values():
            if j%2==0:
                ans+=j
            else:
                if k==1:
                    ans+=j
                    k=0
                else:
                    ans+=(j-1)
                
       
        return ans


        # ch={}
        # ans=0
        # for i in s:
        #     ch[i]=ch.get(i,0)+1
        # if len(ch)==1:
        #     return len(s)
        # for j in ch.values():
        #     if j%2==0:
        #         ans+=j
        #         print(j)
        # if 1 in ch.values():
        #     ans+=1
        # return ans

            
        