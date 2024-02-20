class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2==0:
            p=n//2
            ans=int(pow(5,p,10**9 + 7))*int(pow(4,p,10**9 + 7))
        else:
            e=(n+1)//2
            o=e-1
            ans=int(pow(5,e,10**9 + 7))*int(pow(4,o,10**9 + 7))
        return ans%(10**9 + 7)





        # n=n-1
        # if n==0:
        #     return 5
        # if (n)%2==0:
        #     return 5*self.countGoodNumbers(n)%(10**9+7)
        # else:
        #     return 4*self.countGoodNumbers(n)%(10**9+7)


        
        