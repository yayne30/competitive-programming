class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        sumfive=0
        sumten=0
        for i in range(len (bills)):
            if bills[i]==5:   
                sumfive+=5
            elif bills[i]==10:
                print(sumten)
                if sumfive<=0:
                    return False
                sumten+=10
                sumfive-=5
            else:
                print(sumten)
                if sumten>=10 and sumfive>=5:
                    sumten-=10
                    sumfive-=5
                elif sumten<=0 and sumfive>=15:
                    sumfive-=15
                else:
                    return False



        return True

        