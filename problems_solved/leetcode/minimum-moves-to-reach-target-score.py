class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result=0
        double=0
        if maxDoubles==0:
            return target-1
        else:
            i=maxDoubles
            while i>0 and target>0:
                if target!=1: 
                    result+=target%2
                target=int(target/2)
                double+=1
                i-=1
            result+=(target-1)+double
        return result


        