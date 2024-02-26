class Solution:
    
    def fib(self, n: int) -> int:
        dictt=[0,1]
        for i in range(2,n+1):
            dictt.append(dictt[i-1]+dictt[i-2])
        return dictt[n]
      