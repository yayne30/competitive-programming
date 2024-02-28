class Solution:
    def smallestNumber(self, num: int) -> int:

        nlist = list(map(int,str(abs(num))))
        if num > 0:
            nlist.sort()
        if num<0:
            nlist.sort(reverse=True)
        i=0
        while nlist[i]==0 and len(nlist)>1:
            i+=1
        if  nlist[0]==0:
            nlist[0] , nlist[i] = nlist[i] , nlist[0]
        if num>0:
            return int(''.join(map(str, nlist)))
        elif num<0:
            return int('-'+''.join(map(str, nlist)))
        return 0
        
     

            
        